#!/usr/bin/env python3
"""Refresh the profile README snapshot and the GitHub Stats cards.

The script is intentionally dependency-free so it can run on a stock
GitHub Actions runner. It updates the numbers between the README markers,
regenerates the career card, and refreshes the locally hosted stat cards.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
STATS_DIR = ROOT / "assets" / "stats"
USER = "Xerox563"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

API = "https://api.github.com"
GRAPHQL = f"{API}/graphql"
UA = f"{USER}-profile-stats"


def request(url: str, *, accept: str = "application/vnd.github+json", data: bytes | None = None):
    headers = {
        "Accept": accept,
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": UA,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=45) as response:
        return response.read()


def graphql(query: str, variables: dict | None = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    body = json.loads(request(GRAPHQL, data=payload))
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body["data"]


def fetch_stats() -> dict:
    query = """
    query ProfileStats($login: String!, $search: String!) {
      user(login: $login) {
        repositories(first: 100, privacy: PUBLIC, ownerAffiliations: OWNER) {
          nodes { stargazerCount }
        }
        contributionsCollection {
          totalCommitContributions
          totalPullRequestContributions
          totalIssueContributions
          totalRepositoryContributions
          contributionCalendar { totalContributions }
        }
      }
      search(query: $search, type: ISSUE, first: 100) {
        issueCount
        nodes {
          ... on PullRequest {
            number
            title
            url
            state
            createdAt
            mergedAt
            closedAt
            updatedAt
            repository { nameWithOwner }
          }
        }
      }
    }
    """
    data = graphql(query, {"login": USER, "search": f"author:{USER} is:pr"})
    user = data["user"]
    contributions = user["contributionsCollection"]

    prs = [node for node in data["search"]["nodes"] if node]
    upstream = [
        pr for pr in prs
        if pr["repository"]["nameWithOwner"].split("/", 1)[0].lower() != USER.lower()
    ]
    upstream_merged = [pr for pr in upstream if pr.get("mergedAt")]
    upstream_open = [pr for pr in upstream if pr["state"] == "OPEN"]

    return {
        "stars": sum(repo["stargazerCount"] for repo in user["repositories"]["nodes"]),
        "contributions": contributions["contributionCalendar"]["totalContributions"],
        "commits": contributions["totalCommitContributions"],
        "prs": contributions["totalPullRequestContributions"],
        "issues": contributions["totalIssueContributions"],
        "repos_contributed": contributions["totalRepositoryContributions"],
        "total_prs": len(prs),
        "upstream": upstream,
        "upstream_total": len(upstream),
        "upstream_merged": len(upstream_merged),
        "upstream_open": len(upstream_open),
        "upstream_repos": len({pr["repository"]["nameWithOwner"] for pr in upstream}),
    }


ANIMATION = re.compile(rb"(?<![-\w])animation\s*:[^;\"']*;?")
OPACITY_ZERO = re.compile(rb"(?<![-\w])opacity\s*:\s*0(?:\.0+)?\s*;?")


def sanitize_card(data: bytes) -> bytes:
    """Freeze reveal animations so cards render inside GitHub's image proxy."""
    return ANIMATION.sub(b"", OPACITY_ZERO.sub(b"opacity: 1;", data))


def download_card(filename: str, url: str) -> None:
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    target = STATS_DIR / filename
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
        if b"<svg" not in data[:500] or b"Something went wrong" in data:
            raise ValueError("service returned an error card")
        data = sanitize_card(data)
        if target.exists() and target.read_bytes() == data:
            print(f"unchanged {filename}")
            return
        target.write_bytes(data)
        print(f"updated   {filename}")
    except Exception as exc:  # keep the previous card when a service is down
        print(f"warning: could not refresh {filename}: {exc}", file=sys.stderr)


def refresh_cards() -> None:
    cards = {
        "profile-details.svg": (
            "https://github-profile-summary-cards.vercel.app/api/cards/profile-details"
            f"?username={USER}&theme=radical"
        ),
        "stats.svg": (
            "https://github-profile-summary-cards.vercel.app/api/cards/stats"
            f"?username={USER}&theme=radical"
        ),
        "repos-per-language.svg": (
            "https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language"
            f"?username={USER}&theme=radical"
        ),
        "most-commit-language.svg": (
            "https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language"
            f"?username={USER}&theme=radical"
        ),
        "productive-time.svg": (
            "https://github-profile-summary-cards.vercel.app/api/cards/productive-time"
            f"?username={USER}&theme=radical&utcOffset=5.5"
        ),
        "streak.svg": (
            "https://streak-stats.demolab.com"
            f"?user={USER}&theme=radical&hide_border=false&border_radius=10"
        ),
    }
    for filename, url in cards.items():
        download_card(filename, url)


def career_svg(stats: dict) -> str:
    merged = stats["upstream_merged"]
    circumference = 270.18
    progress = circumference * min(1.0, merged / 15)

    rows = [
        ("Total stars earned", f"{stats['stars']}"),
        ("Commits (last year)", f"{stats['commits']:,}"),
        ("PRs opened (last year)", f"{stats['prs']:,}"),
        ("Issues opened (last year)", f"{stats['issues']:,}"),
        ("Repos contributed to", f"{stats['repos_contributed']:,}"),
    ]
    row_svg = "\n".join(
        f'    <text x="24" y="{72 + i * 21}" class="label">{escape(label)}</text>'
        f'<text x="222" y="{72 + i * 21}" class="value">{escape(value)}</text>'
        for i, (label, value) in enumerate(rows)
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="467" height="195" viewBox="0 0 467 195" role="img" aria-labelledby="title desc">
  <title id="title">Amit Gangwar's GitHub Stats</title>
  <desc id="desc">Career snapshot generated from the GitHub API.</desc>
  <defs>
    <style>
      .sans {{ font-family: "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif; }}
      .label {{ font: 500 12px "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif; fill: #a9fef7; }}
      .value {{ font: 700 12px "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif; fill: #f8d847; }}
      .header {{ font: 700 17px "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif; fill: #fe428e; }}
      .tiny {{ font: 400 8px "Segoe UI", Ubuntu, "Helvetica Neue", sans-serif; fill: #8c88a6; }}
    </style>
  </defs>
  <rect x="1" y="1" width="465" height="193" rx="10" fill="#141321" stroke="#2a2440" stroke-width="1"/>
  <text x="24" y="31" class="header">Amit Gangwar's GitHub Stats</text>
  <text x="24" y="50" class="tiny">auto-refreshed from the GitHub API</text>
{row_svg}
  <circle cx="374" cy="91" r="43" fill="none" stroke="#2a2440" stroke-width="9"/>
  <circle cx="374" cy="91" r="43" fill="none" stroke="#fe428e" stroke-width="9" stroke-linecap="round"
          stroke-dasharray="{progress:.2f} {circumference:.2f}" transform="rotate(-90 374 91)"/>
  <text x="374" y="94" text-anchor="middle" font-family="Segoe UI, Ubuntu, Helvetica Neue, sans-serif"
        font-size="27" font-weight="800" fill="#a9fef7">{merged}</text>
  <text x="374" y="112" text-anchor="middle" class="tiny" letter-spacing="1">MERGED</text>
  <text x="374" y="124" text-anchor="middle" class="tiny" letter-spacing="1">UPSTREAM</text>
  <text x="24" y="179" class="tiny">Generated {datetime.now(timezone.utc):%d %b %Y} · github.com/{USER}</text>
</svg>
'''


def pr_state(pr: dict) -> str:
    if pr.get("mergedAt"):
        return f"merged {pr['mergedAt'][:10]}"
    if pr["state"] == "OPEN":
        return "in review"
    if pr.get("closedAt"):
        return f"closed {pr['closedAt'][:10]}"
    return pr["state"].lower()


def oss_log(stats: dict) -> str:
    prs = sorted(
        stats["upstream"],
        key=lambda pr: pr.get("mergedAt") or pr.get("updatedAt") or pr.get("createdAt") or "",
        reverse=True,
    )
    lines = [
        "| Repository | Pull request | Status |",
        "|---|---|---|",
    ]
    for pr in prs:
        repo = pr["repository"]["nameWithOwner"]
        title = pr["title"].replace("|", "\\|")
        lines.append(f"| [{repo}](https://github.com/{repo}) | [#{pr['number']}: {title}]({pr['url']}) | {pr_state(pr)} |")
    return "\n".join(lines)


def replace_block(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:START -->).*?(<!-- {name}:END -->)", re.S)
    if not pattern.search(text):
        raise RuntimeError(f"missing {name} markers in README.md")
    return pattern.sub(lambda match: f"{match.group(1)}\n{body.strip()}\n{match.group(2)}", text)


def update_readme(stats: dict) -> None:
    text = README.read_text()
    snapshot = f'''<p align="center">
  <code>{stats["contributions"]:,} contributions</code> · <code>{stats["commits"]:,} commits</code><br>
  <code>{stats["upstream_total"]} upstream PRs</code> · <code>{stats["upstream_merged"]} merged</code> · <code>{stats["upstream_repos"]} repos</code>
</p>'''
    oss = f'''<p align="center">
  <strong>{stats["upstream_total"]}</strong> upstream pull requests across <strong>{stats["upstream_repos"]}</strong> repositories.<br>
  <strong>{stats["upstream_merged"]}</strong> merged · <strong>{stats["upstream_open"]}</strong> in review.
</p>'''
    updated = f'<p align="center"><sub>Stats refreshed {datetime.now(timezone.utc):%d %b %Y} by GitHub Actions.</sub></p>'
    text = replace_block(text, "STATS", snapshot)
    text = replace_block(text, "OSS", oss)
    text = replace_block(text, "OSS_LOG", oss_log(stats))
    text = replace_block(text, "UPDATED", updated)
    README.write_text(text)
    print("updated README.md")


def main() -> None:
    if not TOKEN:
        raise SystemExit("GITHUB_TOKEN or GH_TOKEN is required")
    stats = fetch_stats()
    refresh_cards()
    (STATS_DIR / "career.svg").write_text(career_svg(stats))
    print("updated   career.svg")
    update_readme(stats)
    print(json.dumps({key: value for key, value in stats.items() if key != "upstream"}, indent=2))


if __name__ == "__main__":
    main()
