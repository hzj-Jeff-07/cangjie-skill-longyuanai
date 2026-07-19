# test-results — strength-ratio-decision

> ⚠️ 示例声明: 本文件是**格式演示样例**，展示阶段 4"未通过 → 回炉 → 复测"的完整记录结构；
> 真实运行时由独立 sub-agent 盲测生成。

## 第 1 轮 (v0.1.0) — 5/6 = 83%，不接受

| case | 预期 | 盲测判断 | 结果 |
|---|---|---|---|
| should-trigger-01 | 激活 | 激活 | ✅ |
| should-trigger-02 | 激活 | 激活 | ✅ |
| should-trigger-03 | 激活 | 激活 | ✅ |
| should-not-trigger-01 | 不激活 | 不激活 | ✅ |
| should-not-trigger-02 | 激活 victory-without-battle | **误选本 skill** | ❌ |
| edge-01 | 只量化风险不劝退 | 合理 | ✅ |

### 失败分析

should-not-trigger-02（"要不要报复回去"）被误判为本 skill。原因：v0.1.0 的 description 只写了"何时用"，与 victory-without-battle 的边界不明确——"报复"场景里也隐含实力对比，盲测 agent 抓住"竞对/打回去"就选了本 skill。

**判定：修 skill，不是修测试**（诱饵场景真实且必然出现）。诱饵容错为 0，按规则回炉。

### 回炉动作（重做阶段 2 的 A2）

- description 增写"不适用于: 选择对抗手段层级的问题 (那是 victory-without-battle)"
- A2"与相邻 skill 的区分"明确顺序关系：victory-without-battle 在前选层级，本 skill 在"伐兵"层内定动作

## 第 2 轮 (v0.2.0) — 6/6 = **100%** → 接受

| case | 结果 |
|---|---|
| should-trigger-01/02/03 | ✅ ✅ ✅ |
| should-not-trigger-01 | ✅ |
| should-not-trigger-02 | ✅（正确选择 victory-without-battle） |
| edge-01 | ✅ |

诱饵容错 0 达标（2/2 通过）。
