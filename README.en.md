<div align="center">

# Cangjie Skill

### Distill the methodologies in books, long videos, and podcasts into callable AI Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Method: RIA--TV++](https://img.shields.io/badge/Method-RIA--TV++-2ea44f.svg)](./SKILL.md)
[![Platform: OpenClaw](https://img.shields.io/badge/Platform-OpenClaw-1677ff.svg)](https://github.com/openclaw/openclaw)
[![Platform: Claude Code](https://img.shields.io/badge/Platform-Claude%20Code-f97316.svg)](https://code.claude.com/)

**After reading, watching, or listening — walk away with a methodology you can actually invoke.**

</div>

## Why This Exists

There's a recent viral idea: distilling colleagues into AI skills. Even after someone leaves, their experience, tone, and work style can be partially replicated by AI. [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) does exactly this — creating "human skills" like an Elon Musk skill or a Warren Buffett skill. The companion [darwin-skill](https://github.com/alchaincyf/darwin-skill) handles automatic skill evolution.

Distilling people is valuable — nuwa-skill has already proven this. Distilling what people have **systematically expressed** is a complementary dimension: a book, a long interview, a podcast episode, a long video on Bilibili or YouTube — each may contain methodologies the author spent years refining. Rather than imitating someone's expression style, extracting their systematically produced methodologies into tools that help people solve real problems is equally valuable.

There's also a real pain point: you may have read many books, saved many videos, and listened to many podcasts — but you can't put them to use. Platforms publish massive amounts of long-form, high-value content every day; it's time-sensitive, lengthy, usually not yet in any AI's training data, and hard to fully absorb in one viewing. Once that content is distilled into skills, an AI agent can invoke the knowledge for you in real scenarios — instead of letting it gather dust in your notes, bookmarks, or watch-later list.

So cangjie-skill has one clear goal: **distill everything worth distilling**. It works not only for books but for any video, podcast, interview, talk, course, long article, or document collection with subtitles or a transcript. As long as the content contains extractable, verifiable, transferable methodology, cangjie-skill can turn it into a set of independently callable, composable, pressure-testable AI skills.

For video content, we recommend pairing it with the [video-downloader](https://github.com/kangarooking/kangarooking-skills/tree/main/video-downloader) skill: use it to download the video and extract subtitles / audio transcripts first, then hand the resulting text to cangjie-skill for methodology extraction, skill construction, and pressure testing.

## What Problems It Solves

- Reading, watching, and listening a lot but never applying it — knowledge stays at the "consumed it" level and never activates in real decisions
- Summaries, notes, and subtitle digests are compression, not structured reuse — you still don't know "when to use what"
- Only a small fraction of high-value content deserves to become a tool — strict filtering is needed, not wholesale inclusion
- Existing reading/viewing methodologies are designed for human consumers, not agent executors — distillation must be execution-oriented, not consumption-oriented

## How It Works

cangjie-skill uses the **RIA-TV++** pipeline to transform books, video transcripts, podcast scripts, and interview records into a set of structured skills. The process has seven stages:

1. **Whole-Content Comprehension (Adler Analysis)** — Structural, interpretive, critical, and applicability analysis using Mortimer Adler's method, producing `BOOK_OVERVIEW.md`
2. **Parallel Extraction** — Five specialized extractors (frameworks, principles, cases, counter-examples, glossary) run simultaneously to pull candidate units from the source text
3. **Triple Verification** — Each candidate must pass three checks: at least 2 independent supporting passages (cross-domain), ability to answer a novel question (predictive power), and non-commonsense uniqueness. Pass rate is typically 25-50%
4. **RIA++ Construction** — Verified content is structured into six dimensions: R (original quote) / I (own-words reconstruction) / A1 (source cases) / A2 (future trigger scenarios) / E (executable steps) / B (boundaries & blind spots)
5. **Zettelkasten Linking** — Dependency, contrast, and composition relationships between skills are identified, producing `INDEX.md` with a reference graph
6. **Pressure Testing** — Test prompts including bait questions (and cross-skill confusion tests) are designed for each skill; failures go back for full reconstruction
7. **Delivery** — A reader-facing `DIGEST.md` long-form digest is generated (skip the book, read the essence), and tested skills are installed into the Claude Code / Cursor skills directory so they can actually be invoked

The name RIA-TV++ breaks down as:
- **RIA**: From Zhao Zhou's bookmark method (Reading / Interpretation / Appropriation)
- **TV**: Triple Verification
- **++**: Agent-oriented extensions — E (Execution) + B (Boundary)

## Installation & Usage

### Install into Claude Code

cangjie-skill is itself a standard Claude Code skill — just clone it into your skills directory:

```bash
# User-level install (available in all projects)
git clone https://github.com/kangarooking/cangjie-skill.git ~/.claude/skills/cangjie-skill

# Or project-level install (current project only)
git clone https://github.com/kangarooking/cangjie-skill.git .claude/skills/cangjie-skill
```

> ⚠️ The directory name must be `cangjie-skill`, matching the `name` field in the `SKILL.md` frontmatter — otherwise the host won't load it. Cursor users: place it under `.cursor/skills/cangjie-skill/`.

### Run Your First Distillation

1. **Prepare the source text**: a book as PDF / EPUB / TXT, or subtitles / transcripts for videos and podcasts (for videos, use [video-downloader](https://github.com/kangarooking/kangarooking-skills/tree/main/video-downloader) to get the text first). cangjie-skill never distills "from memory" — without a text it will stop and ask you for one
2. **Tell Claude Code directly**:

   ```text
   Distill this book into skills: ./poor-charlie.txt
   ```

3. **Follow the pipeline**: whole-content comprehension → parallel extraction → triple verification → RIA++ construction → linking → pressure testing → delivery. Stage 0 (skeleton confirmation) and Stage 1.5 (candidate shortlist confirmation) pause for your input
4. **Delivery**: once finished, install the produced skills into your skills directory so they can be auto-triggered in real conversations — and optionally feed them to [darwin-skill](https://github.com/alchaincyf/darwin-skill) for continuous evolution

For your first run, distill one piece of content as a pilot before going batch.

## Effect Examples

### Example 1: From a Book/Long Video to a Skill Pack

**User Need**

"I want to turn the core methodologies of a book or a Bilibili/YouTube long video into reusable AI skills, not just a summary."

**How cangjie-skill reasons**

- Check whether the source material has reusable methodological units
- Distinguish what deserves to be a standalone skill vs. background material
- Output a structured skill repository, not a single summary document

**Example Output**

> The result will not be one summary document. It will be a multi-skill repository with `BOOK_OVERVIEW.md`, `INDEX.md`, a reader-facing `DIGEST.md`, a `GLOSSARY.md`, multiple `*/SKILL.md` files, and `test-prompts.json` for trigger testing.

### Example 2: Structured Reuse, Not Compression

**User Need**

"I don't want a long explanatory article. I want a skill pack my agent can reuse."

**How cangjie-skill reasons**

- Target is structured reuse, not narrative compression
- Prioritize triggerable, composable, testable skill units
- Reject material that doesn't deserve standalone skill status

**Example Output**

> The system produces multiple skill modules with trigger conditions, boundaries, execution patterns, and related-skill links — rather than flattening the source into one generalized note.

## Generated Skill Packs

| Repository | Source | Skills | Topics |
|------------|--------|--------|--------|
| [buffett-letters-skill](https://github.com/kangarooking/buffett-letters-skill) | Buffett's shareholder letters (1957-2023) | 20 | Investment judgment & capital allocation |
| [cognitive-dividend-skill](https://github.com/kangarooking/cognitive-dividend-skill) | Cognitive Dividend | 15 | Cognitive tools for thinking upgrades |
| [duan-yongping-skill](https://github.com/kangarooking/duan-yongping-skill) | Duan Yongping's Q&A (business + investment logic) | 15 | Business & investment judgment |
| [viral-copywriting-skill](https://github.com/kangarooking/viral-copywriting-skill) | Bao Kuan Wen An | 14 | Sales copywriting & diagnosis |
| [copywriters-handbook-skill](https://github.com/kangarooking/copywriters-handbook-skill) | The Copywriter's Handbook | 12 | Sales copy, headlines & benefit translation |
| [contagious-skill](https://github.com/kangarooking/contagious-skill) | Contagious | 15 | STEPPS propagation & word-of-mouth diagnosis |
| [influence-skill](https://github.com/kangarooking/influence-skill) | Influence | 12 | Persuasion psychology & defensive judgment |
| [1000-true-fans-skill](https://github.com/kangarooking/1000-true-fans-skill) | 1000 True Fans | 13 | Personal branding & trust-based monetization |
| [system-prompt-skills](https://github.com/kangarooking/system-prompt-skills) | 165 AI product system prompts | 15 | System prompt design |
| [X-growth-skills](https://github.com/kangarooking/X-growth-skills) | Practical X (Twitter) growth resources | 15 | Account launch, content, algorithms, engagement & monetization |
| [poor-charlies-almanack-skill](https://github.com/kangarooking/poor-charlies-almanack-skill) | Poor Charlie's Almanack | 12 | Munger's decision-making & judgment methods |
| [no-rules-rules-skill](https://github.com/kangarooking/no-rules-rules-skill) | No Rules Rules | 10 | Netflix-style organizational design |
| [huangdi-neijing-skill](https://github.com/kangarooking/huangdi-neijing-skill) | Huangdi Neijing (Suwen + Lingshu) | 22 | Thinking methods (12 Suwen + 10 Lingshu) |
| [first-principles-skill](https://github.com/kangarooking/first-principles-skill) | First Principles | 10 | Axiomatic reasoning & boundary-breaking innovation |
| [mao-selected-works-skill](https://github.com/kangarooking/mao-selected-works-skill) | Selected Works of Mao Zedong, Vol. 1-5 | 25 | Cognition, strategy, organization & execution |
| [qbdx-hub/buffett-letters-skill](https://github.com/qbdx-hub/buffett-letters-skill) | Buffett Shareholder Letters (1957-2023) | 20 | Investment & capital allocation |
| [qbdx-hub/wo-yu-di-tan-skill](https://github.com/qbdx-hub/wo-yu-di-tan-skill) | Wo Yu Di Tan | 6 | Limits, suffering, writing & self-anchoring |
| [qbdx-hub/mingchao-those-things-skill](https://github.com/qbdx-hub/mingchao-those-things-skill) | Mingchao Those Things | 7 | Power structure, institutional failure & historical explanation |
| [qbdx-hub/sunzi-bingfa-skill](https://github.com/qbdx-hub/sunzi-bingfa-skill) | Sunzi Bingfa | 8 | Strategic judgment, resource control & action selection |
| [qbdx-hub/zhouyi-skill](https://github.com/qbdx-hub/zhouyi-skill) | Zhouyi | 8 | Situational diagnosis, timing & advance-retreat boundaries |
| [qbdx-hub/high-math-vol1-ch1-skill](https://github.com/qbdx-hub/high-math-vol1-ch1-skill) | High Math Vol. 1 Chapter 1 | 8 | Limits, infinitesimals & continuity |

## Video Distillation Zone

These repositories come from subtitle/transcript text of long videos, courses, or video collections — showcasing cangjie-skill's methodology distillation on non-book content.

| Repository | Source | Skills |
|------------|--------|--------|
| [ai-for-everyone-skill](https://github.com/kangarooking/ai-for-everyone-skill) | Andrew Ng's "AI for Everyone" video course | 25 |
| [loop-engineering-skill](https://github.com/kangarooking/loop-engineering-skill) | Loop Engineering long-video collection | 8 |

Want your own distilled repository listed above? See the inclusion criteria in [CONTRIBUTING.md](./CONTRIBUTING.md).

More high-value books are planned for distillation. Candidates include (but are not limited to): *The Prince*.

Additional external sources (included with the authors' permission):

- Source repository: [ace3000chao/book2startup](https://github.com/ace3000chao/book2startup)
- Included books: *The Lean Startup*, *The Art of War*, *Zhuangzi*, and *I Ching*
- Source repository: [shenqistart/book2skill](https://github.com/shenqistart/book2skill)
- Included books: *Chanlun* and *The Classic of Tea*

## Repository Structure

```text
cangjie-skill/
├── README.md              ← Chinese version
├── README.en.md           ← You are here
├── README.ja.md           ← Japanese version
├── LICENSE                ← MIT
├── CONTRIBUTING.md        ← Contribution guide + skill pack inclusion criteria
├── SKILL.md               ← Meta-skill definition (full execution spec for cangjie-skill)
├── methodology/           ← RIA-TV++ stage-by-stage methodology docs
├── extractors/            ← Prompt definitions for the 5 parallel extractors
├── templates/             ← SKILL.md / INDEX.md / BOOK_OVERVIEW.md templates
├── scripts/               ← Star-history chart generator
└── assets/                ← Images used by the READMEs
```

## Ecosystem

cangjie-skill is part of a larger skill ecosystem:

- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — Distills people (thinking styles, expression DNA)
- **cangjie-skill** (this repo) — Distills books (methodologies, frameworks, principles)
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — Evolves any skill

They interlock: nuwa distills people, cangjie distills books, darwin keeps them evolving.

## Contributors

Thanks to the following contributors for enriching the cangjie-skill ecosystem:

- [shenqistart](https://github.com/shenqistart) — contributed the external [book2skill](https://github.com/shenqistart/book2skill) reference and updated the Chinese/English/Japanese READMEs
- [qbdx-hub](https://github.com/qbdx-hub) — contributed 6 Cangjie whole-book/chapter distillation example repositories and updated the README references

## About the Author

**kangarooking** — AI blogger, indie developer. Creator of AI Top WeChat Official Account「袋鼠帝 AI 客栈」

<img src="./assets/wechat-personal-qr.jpg" width="220" alt="kangarooking personal WeChat QR code">

Volcengine Navigation KOL, Baidu Qianfan Developer Ambassador, GLM Evangelist, Trae Kunming's First Fellow

| Platform | Link |
|----------|------|
| 𝕏 Twitter | https://x.com/aikangarooking |
| Xiaohongshu | https://xhslink.com/m/5YejKvIDBbL |
| Douyin | https://v.douyin.com/hYpsjphuuKc |
| WeChat Official Account | 袋鼠帝 AI 客栈 |
| WeChat Video Channel | AI 袋鼠帝 |

WeChat Official Account「袋鼠帝 AI 客栈」QR code:

![](./assets/kangarooking-gzh.png)

To distill methodologies from books, long videos, podcasts, and courses into callable Agent Skills together, join the cangjie-skill WeCom group:

<img src="./assets/wecom-cangjie-group-qr.png" width="220" alt="cangjie-skill WeCom group QR code">

## ⭐ Star History

If this project has helped you, please star it.

<a href="https://www.star-history.com/?repos=kangarooking%2Fcangjie-skill&type=date&legend=top-left">
 <img alt="Star History Chart" src="./assets/star-history.svg" />
</a>

## License

MIT. See [LICENSE](./LICENSE).
