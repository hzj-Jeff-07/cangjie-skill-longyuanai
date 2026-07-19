# candidates/frameworks.md — framework-extractor 产出

```yaml
- id: f01
  title: 伐谋阶梯（全胜手段排序）
  type: framework
  source_chapter: 谋攻篇 · 第 1-2 段
  source_quote: |
    "上兵伐谋，其次伐交，其次伐兵，其下攻城。攻城之法，为不得已。"
  summary: |
    面对冲突时, 手段按破坏成本从低到高排成阶梯:
    挫败对方的计划 (伐谋) → 瓦解对方的联盟 (伐交) → 正面交战 (伐兵) → 强攻坚城 (攻城)。
    永远从阶梯低端开始尝试, 只有低端手段确认不可行才向上升级;
    最高破坏的手段是"不得已", 不是默认选项。
    背后的价值标准是"全胜": 完整地赢优于打烂了赢, 因为破坏本身是己方成本。
  tags: [strategy, conflict, escalation, negotiation]

- id: f02
  title: 十围五攻（实力比驱动的行动选择）
  type: framework
  source_chapter: 谋攻篇 · 第 3 段
  source_quote: |
    "十则围之，五则攻之，倍则分之，敌则能战之，少则能逃之，不若则能避之。故小敌之坚，大敌之擒也。"
  summary: |
    先量化敌我实力比, 再由比值决定可行动作:
    10:1 围而不打 / 5:1 正面攻 / 2:1 设法分割对方 / 1:1 可以一战 /
    劣势则脱离接触 / 悬殊则彻底回避。
    核心是"动作集合由实力比决定", 而不是由意志决定 —
    弱势方硬拼 ("小敌之坚") 的结局是被强者俘获 ("大敌之擒")。
  tags: [strategy, resource, decision, competition]

- id: f03
  title: 知彼知己（决策前信息完备度审计）
  type: framework
  source_chapter: 谋攻篇 · 末段
  source_quote: |
    "知彼知己者，百战不殆；不知彼而知己，一胜一负；不知彼不知己，每战必殆。"
  summary: |
    把重大决策前的信息状态分成四象限: 知彼×知己 / 不知彼×知己 /
    知彼×不知己 / 都不知, 并给出对应的胜率预期 (不殆 / 一半 / 必败)。
    可操作化为: 行动前分别清点"我对对方知道什么"和"我对自己知道什么",
    两边都及格才进入行动决策; 缺哪边先补哪边。
  tags: [decision, information, self-awareness, risk]
```

## 自检

- [x] 每条都在原文有明确根据
- [x] 每条都是可迁移的思考结构
- [x] 原文引用 ≤150 字/段
- [x] 均已标 tag，未做筛选（留给阶段 1.5）
