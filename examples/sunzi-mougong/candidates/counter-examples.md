# candidates/counter-examples.md — counter-example-extractor 产出

```yaml
- id: ce01
  title: 蚁附攻城（情绪驱动的强攻）
  type: counter-example
  source_chapter: 谋攻篇 · 第 2 段
  source_quote: |
    "将不胜其忿而蚁附之，杀士三分之一而城不拔者，此攻之灾也。"
  summary: |
    将领被愤怒支配, 在攻城条件不具备时驱使士兵爬城强攻,
    损失三分之一兵力仍拿不下城。失败机制: 情绪替代了成本计算,
    把阶梯最底端的手段当成了发泄出口。
    预警信号: 决策理由从"划算"变成"咽不下这口气"。
  tags: [counter-example, emotion, escalation]

- id: ce02
  title: 君之三患（远程遥控指挥）
  type: counter-example
  source_chapter: 谋攻篇 · 第 4 段
  source_quote: |
    "不知军之不可以进而谓之进，不知军之不可以退而谓之退，是谓縻军；不知三军之事而同三军之政者，则军士惑矣。"
  summary: |
    三种上位者干预导致失败: 不懂进退条件却下进退令 (縻军)、
    不懂军务却参与军政 (惑军)、不懂权变却干预任命 (疑军)。
    共同机制: 决策权与一线信息分离。预警信号: "乱军引胜" —
    自乱其军, 把胜利让给对手。
  tags: [counter-example, organization, micromanagement]

- id: ce03
  title: 小敌之坚（劣势死撑）
  type: counter-example
  source_chapter: 谋攻篇 · 第 3 段
  source_quote: |
    "故小敌之坚，大敌之擒也。"
  summary: |
    实力劣势时选择硬顶而不是脱离, 结局是被俘获。
    失败机制: 把"坚持"当成美德, 用意志对冲实力差。
    (与 f02 同源, 作为 f02 的 B 段素材。)
  tags: [counter-example, risk, willpower]
```

## 自检

- [x] 每条都是作者明确警告的失败模式，有原文根据
- [x] 引用 ≤150 字/段，未做筛选
