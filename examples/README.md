# examples/ — 端到端产出示例

这里存放 cangjie-skill 流水线的**完整产出示例**，让你在跑第一次蒸馏之前，直观看到每个阶段的产物长什么样。

## sunzi-mougong — 《孙子兵法·谋攻篇》

一个刻意做小的完整示例：蒸馏对象只有一篇公版短文（约 450 字），但走完了全部阶段，产出所有规定文件：

| 阶段 | 产物 | 看什么 |
|---|---|---|
| 0 整书理解 | [BOOK_OVERVIEW.md](./sunzi-mougong/BOOK_OVERVIEW.md) | Adler 四步如何填、批判段怎么写 |
| 1 并行提取 | [candidates/](./sunzi-mougong/candidates/) | 5 个 extractor 各自的产出格式（含 case-extractor 空产出的诚实写法） |
| 1.5 三重验证 | [verified.md](./sunzi-mougong/verified.md) · [rejected/](./sunzi-mougong/rejected/) | V1/V2/V3 判定怎么记录、淘汰理由怎么写 |
| 2 RIA++ 构造 | [victory-without-battle/SKILL.md](./sunzi-mougong/victory-without-battle/SKILL.md) 等 | 六段结构 + frontmatter 的完整样例 |
| 3 链接 | [INDEX.md](./sunzi-mougong/INDEX.md) · [GLOSSARY.md](./sunzi-mougong/GLOSSARY.md) | 引用图、推荐学习顺序、术语词典 |
| 4 压力测试 | 各 skill 目录下 `test-prompts.json` · `test-results.md` | 三类测试用例 + 跨 skill 混淆诱饵怎么设计 |
| 5 交付 | [DIGEST.md](./sunzi-mougong/DIGEST.md) · [PIPELINE_STATE.md](./sunzi-mougong/PIPELINE_STATE.md) | 精华长文与断点续跑状态文件 |

### 与真实运行的差异（诚实声明）

- 蒸馏对象是**单篇短章**而非整书，所以 V1 跨域验证的"独立语境"以篇内不同段落、不同对象为准（整书蒸馏时应跨章节）
- `test-results.md` 中的测试记录是**格式演示样例**，不是真实独立 sub-agent 盲测的存档——真实运行时由流水线阶段 4 生成
- DIGEST 约 1500 字，符合"短内容不必硬凑 5000 字"的规则

### 怎么用这个示例

- 想知道"我的产出是否合格"→ 对照这里同名文件的结构和颗粒度
- 想改模板 → 先在这里跑一遍新模板，确认各阶段仍能咬合
- 想给 darwin-skill 喂测试 → 三个 skill 的 `test-prompts.json` 都是兼容格式
