# 贡献指南

感谢你对 cangjie-skill 的关注。本项目欢迎两类贡献：**改进方法论本身**，以及**提交你用 cangjie-skill 蒸馏出的 skill 仓库**（收录进 README 列表）。

## 一、改进方法论 / 文档

- `SKILL.md` 是元 skill 的执行规范，`methodology/` 是各阶段的设计说明，`extractors/` 是 5 个提取器的 prompt，`templates/` 是产出模板。四者需要保持一致：改了流程，请同步检查其余三处。
- README 有中（`README.md`）、英（`README.en.md`）、日（`README.ja.md`）三个版本。**改任何一个版本的内容，请同步另外两个版本**——历史上三个版本漂移过，请不要再让它发生。
- 提交前请自查：文档内引用的文件路径真实存在；对外链接可访问。

## 二、提交蒸馏仓库（收录标准）

README 的「已生成的 skill packs」「视频蒸馏区」列表接受社区提交。为了保证列表的含金量与项目"严格质量门"的定位一致，收录需满足以下标准：

### 硬性要求

1. **完整的流水线产物**：仓库中包含 `BOOK_OVERVIEW.md`、`INDEX.md`、`GLOSSARY.md`，以及每个 skill 独立目录下的 `SKILL.md`
2. **六段结构**：每个 SKILL.md 具备完整的 R / I / A1 / A2 / E / B 六段
3. **测试文件**：每个 skill 附带 darwin 兼容的 `test-prompts.json`，包含 should_trigger / should_not_trigger（诱饵）/ edge_case 三类用例，且至少 1 条诱饵是同仓库兄弟 skill 的跨 skill 混淆测试
4. **测试结果**：附 `test-results.md` 或在 README 中说明压测通过率（诱饵容错为 0）
5. **可追溯**：每个 skill 有原文引用并标注出处（章节 / 页码 / 时间戳 / 集数），单段引用 ≤150 字（英文 ≤100 词）
6. **版权底线**：不得包含大段原文转载；引用遵守上述限额；来源信息（书名/作者/出版年，或视频标题/作者/发布时间）完整可查

### 建议（非硬性）

- 附 `DIGEST.md` 精华长文，方便读者不装 skill 也能受益
- 附 `rejected/` 淘汰记录，展示三重验证的筛选过程

### 提交方式

发 PR 修改 `README.md` 的对应表格（同步 `README.en.md` 与 `README.ja.md`），在 PR 描述中简要说明：

- 蒸馏来源（书 / 视频 / 播客 / 课程）与元信息
- skill 数量与压测通过情况
- 是否使用 cangjie-skill 流水线（或等效流程）产出

维护者会抽查 2–3 个 skill 的六段完整性与测试文件后合并。

## 三、其他约定

- 提交信息用简洁的祈使句，前缀风格参考现有历史（`docs:` / `fix:` / `feat:`）
- 大文件（图片等）入库前请压缩；README 引用仓库内图片一律用相对路径（`./assets/...`），不要用 raw.githubusercontent.com 绝对链接
