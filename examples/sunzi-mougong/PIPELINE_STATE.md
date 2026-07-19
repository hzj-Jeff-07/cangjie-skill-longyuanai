# PIPELINE_STATE — 《孙子兵法·谋攻篇》

> 断点续跑状态文件。每完成一个阶段更新一次。

- **当前阶段**: ✅ 全部完成（阶段 0–5）
- **内容元信息**: 《孙子兵法》谋攻篇 · 孙武 · 春秋末期（公版文本）
- **文本来源**: 公版原文（约 450 字）

## 阶段进度

- [x] 阶段 0 — 整书理解 → `BOOK_OVERVIEW.md`（用户已确认骨架）
- [x] 阶段 1 — 并行提取 → `candidates/` 5 份（case-extractor 产出为空，已注明原因）
- [x] 阶段 1.5 — 三重验证 → `verified.md` 通过 3 个 / `rejected/` 淘汰 1 个（用户已确认名单）
- [x] 阶段 2 — RIA++ 构造 → 3 个 skill 的 SKILL.md
- [x] 阶段 3 — Zettelkasten 链接 → `INDEX.md` + `GLOSSARY.md`，A2 相邻区分已回填
- [x] 阶段 4 — 压力测试 → 3 份 `test-prompts.json` + `test-results.md`，全部通过
- [x] 阶段 5 — 交付 → `DIGEST.md` 已生成

## 各 skill 状态

| skill | 阶段 2 | 阶段 3 | 阶段 4 |
|---|---|---|---|
| victory-without-battle | ✅ | ✅ | ✅ 6/6 |
| strength-ratio-decision | ✅ | ✅ | ✅ 6/6（首轮 5/6，回炉后通过） |
| know-both-sides | ✅ | ✅ | ✅ 6/6 |

## 下一步

无（流水线完成）。如需进化: `darwin evolve examples/sunzi-mougong/`
