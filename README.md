<div align="center">
  <img src="assets/hero-dark.svg#gh-dark-mode-only" alt="Amit Gangwar, software engineer" width="100%">
  <img src="assets/hero-light.svg#gh-light-mode-only" alt="Amit Gangwar, software engineer" width="100%">
</div>

<p align="center">
  <a href="https://portfolio-of-amit.vercel.app/">Portfolio</a> ·
  <a href="https://github.com/Xerox563">GitHub</a> ·
  <a href="https://linkedin.com/in/amit-g-a63174250">LinkedIn</a> ·
  <a href="mailto:gangwaramit449@gmail.com">Email</a>
</p>

<!-- STATS:START -->
<p align="center">
  <code>908 contributions</code> · <code>707 commits</code><br>
  <code>16 upstream PRs</code> · <code>10 merged</code> · <code>10 repos</code>
</p>
<!-- STATS:END -->

## 01 / ABOUT

I am a software engineer at **i8CLOUD**, building AI systems, backend platforms, and developer tools. I like the unglamorous parts: idempotent pipelines, merge semantics, retries, and the moment a fix lands upstream.

**Now:** shipping agentic AI and Odoo integrations at i8CLOUD, contributing upstream in Rust, TypeScript, C++, and Go, and going deeper into distributed systems.

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 02 / OPEN SOURCE

<p align="center">
  <img src="assets/oss-signal.svg" alt="Open source contribution areas" width="100%">
</p>

Open source is where the code has to survive someone else's review. I contribute to the tools I use: Rust merge semantics, Recharts visualization, Gazebo namespaces, and Go infrastructure.

<!-- OSS:START -->
<p align="center">
  <strong>16</strong> upstream pull requests across <strong>10</strong> repositories.<br>
  <strong>10</strong> merged · <strong>6</strong> in review.
</p>
<!-- OSS:END -->

### Featured upstream work

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

#### [keepass-rs](https://github.com/sseemayer/keepass-rs) · `RUST` · `IN REVIEW`

**Ancestor-aware three-way merge for KDBX databases**

Designed the merge from first principles: one-sided changes apply even when their timestamps are older, true conflicts warn, and additions, deletions, moves, entry history, and custom icons are covered. Added 13 regression tests.

[Read PR #390 →](https://github.com/sseemayer/keepass-rs/pull/390)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

#### [Recharts](https://github.com/recharts/recharts) · `TYPESCRIPT` · `MERGED + IN REVIEW`

**Nightingale and Wind Rose chart examples**

Merged the Nightingale example. The Wind Rose example ships with nine visual-regression baselines across Chromium, Firefox, WebKit, light and dark themes, plus a three-series legend and corrected compass labels.

[PR #8095 →](https://github.com/recharts/recharts/pull/8095) · [PR #8118 →](https://github.com/recharts/recharts/pull/8118)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

#### [Gazebo Sim](https://github.com/gazebosim/gz-sim) · `C++` · `5 MERGED + 1 IN REVIEW`

**Namespace support across six simulation systems**

CameraVideoRecorder, PosePublisher, DetachableJoint, FreeSpaceExplorer, PerformerDetector, and KineticEnergyMonitor.

[PR #4124 →](https://github.com/gazebosim/gz-sim/pull/4124) · [Merged PRs →](https://github.com/pulls?q=is%3Apr+author%3AXerox563+is%3Amerged+repo%3Agazebosim%2Fgz-sim)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<sub>ALSO MERGED</sub> [ceph-csi #6677](https://github.com/ceph/ceph-csi/pull/6677) · [ORAS #2271](https://github.com/oras-project/oras/pull/2271) · [LangChain docs #7017](https://github.com/langchain-ai/docs/pull/7017)

<sub>IN REVIEW</sub> [APITable #1823](https://github.com/apitable/apitable/pull/1823) · [StyleX #1997](https://github.com/meta/stylex/pull/1997) · [RocketRide #2818](https://github.com/rocketride-org/rocketride-server/pull/2818)

<details>
<summary><strong>Full upstream merge log</strong></summary>

<!-- OSS_LOG:START -->
| Repository | Pull request | Status |
|---|---|---|
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | [#4124: Add namespace support to CameraVideoRecorder](https://github.com/gazebosim/gz-sim/pull/4124) | in review |
| [memtomem/memtomem](https://github.com/memtomem/memtomem) | [#3013: feat(cli): add help examples for config and session groups](https://github.com/memtomem/memtomem/pull/3013) | in review |
| [recharts/recharts](https://github.com/recharts/recharts) | [#8118: docs(www): add multi-series wind rose example](https://github.com/recharts/recharts/pull/8118) | merged 2026-10-29 |
| [sseemayer/keepass-rs](https://github.com/sseemayer/keepass-rs) | [#390: feat(merge): add ancestor-aware three-way merge](https://github.com/sseemayer/keepass-rs/pull/390) | in review |
| [recharts/recharts](https://github.com/recharts/recharts) | [#8095: docs(www): add Nightingale chart example](https://github.com/recharts/recharts/pull/8095) | merged 2026-10-28 |
| [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | [#2818: feat(nodes): add store_lancedb, an embedded LanceDB vector store](https://github.com/rocketride-org/rocketride-server/pull/2818) | in review |
| [meta/stylex](https://github.com/meta/stylex) | [#1997: [babel-plugin] Polyfill logical border radius properties](https://github.com/meta/stylex/pull/1997) | in review |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | [#4127: Add namespace support to KineticEnergyMonitor](https://github.com/gazebosim/gz-sim/pull/4127) | merged 2026-10-27 |
| [apitable/apitable](https://github.com/apitable/apitable) | [#1823: feat: add theme toggle to space management](https://github.com/apitable/apitable/pull/1823) | in review |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | [#4126: Add namespace support to PerformerDetector](https://github.com/gazebosim/gz-sim/pull/4126) | merged 2026-10-27 |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | [#4121: Add namespace support to PosePublisher](https://github.com/gazebosim/gz-sim/pull/4121) | merged 2026-10-27 |
| [ceph/ceph-csi](https://github.com/ceph/ceph-csi) | [#6677: util: add --config flag for the Ceph-CSI config file path](https://github.com/ceph/ceph-csi/pull/6677) | merged 2026-10-26 |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | [#4125: Add namespace support to FreeSpaceExplorer](https://github.com/gazebosim/gz-sim/pull/4125) | merged 2026-10-26 |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | [#4123: Add namespace support to DetachableJoint](https://github.com/gazebosim/gz-sim/pull/4123) | merged 2026-10-26 |
| [oras-project/oras](https://github.com/oras-project/oras) | [#2271: ci: publish build provenance attestations for release artifacts](https://github.com/oras-project/oras/pull/2271) | merged 2026-10-23 |
| [langchain-ai/docs](https://github.com/langchain-ai/docs) | [#7017: [FIX] fixed BaseMessage import in functional API chatbot example](https://github.com/langchain-ai/docs/pull/7017) | merged 2026-10-23 |
<!-- OSS_LOG:END -->

</details>

[All pull requests →](https://github.com/pulls?q=is%3Apr+author%3AXerox563)

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 03 / SELECTED WORK

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

### [MindVault](https://mindvault7.vercel.app/) · Chat with your documents

A smart assistant for your own documents. Upload your files or connect Google Drive, Slack, and Notion, then ask questions in plain English and get answers that point back to the exact source.

[Live](https://mindvault7.vercel.app/) · [Code](https://github.com/Xerox563/MindVault)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

### [Luminal](https://luminal-six.vercel.app/) · Smart AI model picker

A smart switchboard for AI chat. It decides which AI model should answer each question, using cheap models for easy ones and strong models for hard ones, so you get good answers without overspending.

[Live](https://luminal-six.vercel.app/) · [Code](https://github.com/Xerox563/Luminal)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

### [Notification System](https://github.com/Xerox563/Notification-system) · Email, SMS and push sender

A service that sends emails, SMS, and push notifications for an app. It makes sure every message goes out, retries when something fails, and never sends the same message twice.

[Code](https://github.com/Xerox563/Notification-system)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

### [Zero](https://github.com/Xerox563/Project_zero) · Voice-controlled desktop assistant

A Jarvis-style assistant that sits on top of your Windows desktop and wakes up when you say "Hey Zero". Ask it for live news, weather, or market updates, watch a voice-controlled News TV, or open an article and chat about it. Simple commands run instantly, and anything else goes to an AI that can see your screen.

[Code](https://github.com/Xerox563/Project_zero)

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 04 / TOOLBOX

- **AI systems:** LangChain · LangGraph · CrewAI · RAG · pgvector · ChromaDB · MCP · n8n
- **Backend:** Python · FastAPI · Node.js · Express · RabbitMQ · Celery · WebSockets
- **Frontend:** React · Next.js · TypeScript · Tailwind · Redux · Three.js
- **Data and infra:** PostgreSQL · MongoDB · Redis · Docker · AWS · CI/CD · Linux
- **Languages:** Python · TypeScript · JavaScript · Rust · C++ · Go · Java · SQL

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 05 / EXPERIENCE

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

**i8CLOUD** · Software Developer · Jul 2025 - Present

- Developed an AWS event-driven LightSpeed-to-Odoo sync for about 12,000 SKUs across 10+ stores. Handled 3,000+ daily events with under 30s latency and idempotent processing.
- Deployed an MCP-integrated Claude assistant for Odoo's Time Off module, serving 200+ employees. Automated about 300 monthly leave requests and end-of-month balance notifications.
- Built an OCR pipeline extracting invoice and POS data into Odoo with 95%+ accuracy. Processed about 2,000 monthly documents, cutting manual entry time by 40% for finance teams.
- Shipped a RAG pipeline (LangChain, pgvector) for semantic search over 1,000+ candidate profiles. Integrated Claude via MCP, reducing recruitment screening time by 35%.
- Engineered an AWS SQS + Lambda pipeline for async PDF ingestion of about 400 daily documents. Enabled real-time Q&A with under 5s processing latency and costs of about $0.005 per query.

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<table width="100%">
<tr>
<td width="100%">

<img src="assets/glow.svg" alt="" width="100%">

**WittyHat** · Software Developer Intern · May 2025 - Jun 2025

- Built Python backend services for YouTube automation with Celery workers, Google OAuth, and event-driven pipelines.
- Cut page load time from 3.2s to 2.2s with lazy loading, caching, and MongoDB indexing.

<img src="assets/glow.svg" alt="" width="100%">

</td>
</tr>
</table>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 06 / SIGNALS

| 1,600+ | 1654 | 1872 | 8.01 | Winner | 3x |
|:---:|:---:|:---:|:---:|:---:|:---:|
| DSA problems | Codeforces Expert | LeetCode Knight | CGPA | i8CLOUD Hackathon | Pat on the Back |

B.Tech in Information Technology, Bundelkhand Institute of Engineering and Technology, Jhansi · 2021 - 2025

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 07 / GITHUB STATS

<p align="center">
  <img src="assets/icons/chart.svg" width="28" height="28" alt=""> <strong>GITHUB STATS</strong><br>
  <sub>Live profile telemetry, refreshed weekly by GitHub Actions.</sub>
</p>

<p align="center">
  <img src="assets/stats/profile-details.svg" alt="GitHub profile details, contributions in the last year" height="170">
  <img src="assets/stats/stats.svg" alt="GitHub stats, stars, commits, pull requests, issues, and repositories" height="170">
</p>

<p align="center">
  <img src="assets/stats/repos-per-language.svg" alt="Top languages by repository" height="145">
  <img src="assets/stats/most-commit-language.svg" alt="Top languages by commit" height="145">
  <img src="assets/stats/productive-time.svg" alt="Commits by time of day" height="145">
</p>

<p align="center">
  <img src="assets/stats/career.svg" alt="Amit Gangwar's career stats" height="170">
  <img src="assets/stats/streak.svg" alt="Current and longest contribution streak" height="170">
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="100%"></p>

## 08 / CONTACT

<p align="center"><strong>Building something in AI infrastructure, developer tools, or open source? Let's build something worth merging.</strong></p>

<p align="center">
  <a href="https://portfolio-of-amit.vercel.app/">Portfolio</a> ·
  <a href="https://github.com/Xerox563">GitHub</a> ·
  <a href="https://linkedin.com/in/amit-g-a63174250">LinkedIn</a> ·
  <a href="mailto:gangwaramit449@gmail.com">Email</a>
</p>

<!-- UPDATED:START -->
<p align="center"><sub>Stats refreshed 09 Nov 2026 by GitHub Actions.</sub></p>
<!-- UPDATED:END -->
