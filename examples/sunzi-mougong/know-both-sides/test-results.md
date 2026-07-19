# test-results — know-both-sides

> ⚠️ 示例声明: 本文件是**格式演示样例**，展示阶段 4 产出应有的记录结构；
> 真实运行时由独立 sub-agent 盲测生成。

- **测试方式**: 独立 sub-agent 盲测（隐藏 type / expected_behavior / notes；提供整包 3 个 skill 的 name + description 做选择题）
- **通过率**: 6/6 = **100%** → 接受

| case | 预期 | 盲测判断 | 结果 |
|---|---|---|---|
| should-trigger-01 | 激活 | 激活（命中"赌一把"+ 知彼空白） | ✅ |
| should-trigger-02 | 激活 | 激活（识别知己栏未审） | ✅ |
| should-trigger-03 | 激活 | 激活（命中 do I know enough） | ✅ |
| should-not-trigger-01 | 不激活 | 不激活（信息已备，纯权衡） | ✅ |
| should-not-trigger-02 | 激活 victory-without-battle | 选择 victory-without-battle（信息已备 + 手段选择） | ✅ |
| edge-01 | 不激活 | 不激活（可逆小决策） | ✅ |

## 失败分析

无。诱饵容错 0 达标（2/2 通过）。
