<div align="center">

# Cangjie Skill

### 本・長編動画・ポッドキャストの方法論を、呼び出し可能な AI Skills に蒸留する

[![License: MIT](https://img.shields.io/badge/License-MIT-f5c542.svg)](./LICENSE)
[![Method: RIA--TV++](https://img.shields.io/badge/Method-RIA--TV++-2ea44f.svg)](./SKILL.md)
[![Platform: OpenClaw](https://img.shields.io/badge/Platform-OpenClaw-1677ff.svg)](https://github.com/openclaw/openclaw)
[![Platform: Claude Code](https://img.shields.io/badge/Platform-Claude%20Code-f97316.svg)](https://code.claude.com/)

**読んだ後、観た後、聴いた後に、呼び出せる方法論を持ち帰る。**

</div>

## なぜこれを作ったのか

最近バズったアイデアがあります：同僚を AI スキルに蒸留する。人が離職しても、その人の経験、口調、仕事のスタイルが AI によってある程度再現できる。[nuwa-skill](https://github.com/alchaincyf/nuwa-skill) はまさにこれを行う——イーロン・マスク skill やウォーレン・バフェット skill のような「人間 skill」を生成します。コンパニオンの [darwin-skill](https://github.com/alchaincyf/darwin-skill) はスキルの自動進化を担当します。

人を蒸留することは価値があります——nuwa-skill がすでにそれを証明しています。その人が**体系的に表現してきたコンテンツ**を蒸留することは、補完的な次元です：一冊の本、長時間のインタビュー、ポッドキャストの一エピソード、Bilibili や YouTube の長編動画——いずれも著者が長い時間をかけて磨き上げた方法論が凝縮されている可能性があります。人の表現スタイルを真似するのではなく、体系的に出力された方法論を実問題を解決するツールとして抽出することも、同様に価値のあることです。

また、リアルなペインポイントもあります：多くの本を読み、多くの動画を保存し、多くのポッドキャストを聴いても、活用できない。各プラットフォームには毎日大量の長編有益コンテンツが投稿され、時効性が高く、内容も長い。AI の学習データにまだ含まれていないことが多く、一度の視聴で完全に吸収するのも難しい。こうしたコンテンツをスキルに蒸留すれば、AI エージェントが実際のシナリオでその知識を呼び出してくれる——ノートやブックマーク、「後で見る」リストで埃をかぶせる代わりに。

だから cangjie-skill の目標は一つ：**蒸留する価値のあるすべての高価値コンテンツを蒸留する**。本だけでなく、字幕・書き起こしテキストのある動画、ポッドキャスト、インタビュー、講演、コース、長文記事、資料集にも適用できます。コンテンツに抽出可能・検証可能・転用可能な方法論が存在する限り、cangjie-skill はそれを独立して呼び出し可能、組み合わせ可能、ストレステスト可能な AI スキルパックに変えられます。

動画コンテンツを蒸留する場合は、[video-downloader](https://github.com/kangarooking/kangarooking-skills/tree/main/video-downloader) skill との併用を推奨します：まず動画のダウンロードと字幕・音声書き起こしの抽出を行い、得られたテキストを cangjie-skill に渡して方法論抽出・スキル化・ストレステストを行います。

## 解決する問題

- 多くの本・動画・ポッドキャストを消費しても活用できない——知識が「読んだ/観た/保存した」レベルに留まり、実際の意思決定で活性化されない
- 要約・メモ・字幕整理は圧縮であって、構造化された再利用ではない——「いつ何を使うべきか」が分からないまま
- 高価値コンテンツの中で本当にツールになる価値のある内容はごく一部——厳格なフィルタリングが必要で、全部入りではない
- 既存の読書・視聴方法論は人間の消費者向けで、エージェントの実行者向けではない——実行志向の蒸留が必要

## どう動くか

cangjie-skill は **RIA-TV++** パイプラインを使用して、書籍・動画書き起こし・ポッドキャスト原稿・インタビュー記録などの生テキストを構造化されたスキルのセットに変換します。7段階のプロセスです：

1. **全体コンテンツ理解（Adler分析）** — モーティマー・アドラーの分析方法で、コンテンツ全体を構造・解釈・批判・応用の4ステップで分解し、`BOOK_OVERVIEW.md` を生成
2. **並行抽出** — 5つの専門エクストラクター（フレームワーク、原則、事例、反例、用語）が同時に実行され、原文から候補ユニットを抽出
3. **三重検証** — 各候補は3つのチェックを通過する必要があります：原文に少なくとも2つの独立した裏付けがあるか（クロスドメイン）、新しい質問に答えられるか（予測力）、常識ではないか（独自性）。合格率は通常25〜50%
4. **RIA++ 構築** — 検証済みの内容を6つの次元に構造化：R（原文引用）/ I（自分の言葉での再構築）/ A1（原典の事例）/ A2（将来のトリガーシーン）/ E（実行可能ステップ）/ B（境界と盲点）
5. **ツェッテルカステン連携** — スキル間の依存、対比、構成関係を特定し、参照グラフ付きの `INDEX.md` を生成
6. **ストレステスト** — 各スキルに囮問題（スキル間混同テストを含む）を含むテストプロンプトを設計。不合格は全面的に再構築
7. **デリバリー** — 読者向けの `DIGEST.md`（本を読まずにエッセンスを読める長文ダイジェスト）を生成し、テストに合格したスキルを Claude Code / Cursor の skills ディレクトリにインストールして、実際に呼び出せるようにする

RIA-TV++ の名前の由来：
- **RIA**：趙周のブックマーク法（Reading / Interpretation / Appropriation）
- **TV**：Triple Verification（三重検証）
- **++**：エージェント実行向けの拡張——E（Execution）+ B（Boundary）

## インストールと使い方

### Claude Code へのインストール

cangjie-skill 自体が標準的な Claude Code skill です。skills ディレクトリにクローンするだけで使えます：

```bash
# ユーザーレベル（すべてのプロジェクトで利用可能）
git clone https://github.com/kangarooking/cangjie-skill.git ~/.claude/skills/cangjie-skill

# またはプロジェクトレベル（現在のプロジェクトのみ）
git clone https://github.com/kangarooking/cangjie-skill.git .claude/skills/cangjie-skill
```

> ⚠️ ディレクトリ名は `SKILL.md` frontmatter の `name` フィールドと一致する `cangjie-skill` である必要があります。一致しないとホストが読み込みません。Cursor ユーザーは `.cursor/skills/cangjie-skill/` に配置してください。

### 初めての蒸留

1. **コンテンツのテキストを準備**：書籍の PDF / EPUB / TXT、または動画・ポッドキャストの字幕・書き起こし（動画は先に [video-downloader](https://github.com/kangarooking/kangarooking-skills/tree/main/video-downloader) でテキストを取得することを推奨）。cangjie-skill は「記憶に頼った」蒸留を行いません——テキストがなければ停止して要求します
2. **Claude Code に直接伝える**：

   ```text
   この本をスキルに蒸留して：./poor-charlie.txt
   ```

3. **パイプラインに従う**：全体理解 → 並行抽出 → 三重検証 → RIA++ 構築 → 連携 → ストレステスト → デリバリー。ステージ0（骨格確認）とステージ1.5（候補リスト確認）では、あなたの確認のために一時停止します
4. **デリバリー**：完了後、生成されたスキルを skills ディレクトリにインストールすれば、実際の会話で自動的にトリガーされます。[darwin-skill](https://github.com/alchaincyf/darwin-skill) に渡して継続的に進化させることもできます

初回はまず1つのコンテンツでパイロット蒸留を行い、フローを確認してからバッチ処理することを推奨します。

## 効果例

### 例1：本・長編動画からスキルパックへ

**ユーザーの要望**

「本や Bilibili/YouTube の長編動画のコア方法論を再利用可能な AI スキルにしたい。要約ではなく。」

**cangjie-skill の判断**

- 元資料に再利用可能な方法論ユニットがあるか確認
- スタンドアロンのスキルに値するものと背景情報を区別
- 単一の要約ではなく、構造化されたスキルリポジトリを出力

**出力例**

> 結果は1つの要約ファイルではなく、`BOOK_OVERVIEW.md`、`INDEX.md`、読者向けの `DIGEST.md`、`GLOSSARY.md`、複数の `*/SKILL.md`、トリガー検証用の `test-prompts.json` を含む multi-skill リポジトリになります。

### 例2：圧縮ではなく、構造化再利用

**ユーザーの要望**

「長い説明文が欲しいのではなく、エージェントが再利用できるスキルパックが欲しい。」

**cangjie-skill の判断**

- 目標は構造化再利用であり、物語の圧縮ではない
- トリガー可能、組み合わせ可能、テスト可能なスキルユニットを優先
- スタンドアロンのスキルに値しない素材は落とす

**出力例**

> システムはトリガー条件、境界、実行パターン、関連スキルリンクを持つ複数のスキルモジュールを生成します——全体を1つの汎用的なノートに平坦化するのではなく。

## 生成済みスキルパック

| リポジトリ | 元資料 | スキル数 | テーマ |
|------------|--------|----------|--------|
| [buffett-letters-skill](https://github.com/kangarooking/buffett-letters-skill) | バフェットの株主への手紙（1957-2023） | 20 | 投資判断と資本配分 |
| [cognitive-dividend-skill](https://github.com/kangarooking/cognitive-dividend-skill) | 『認知紅利』 | 15 | 思考アップグレードの認知ツール |
| [duan-yongping-skill](https://github.com/kangarooking/duan-yongping-skill) | 段永平の投資Q&A（ビジネス+投資ロジック） | 15 | ビジネスと投資の判断 |
| [viral-copywriting-skill](https://github.com/kangarooking/viral-copywriting-skill) | 『爆款文案』 | 14 | 販売コピーライティングと診断 |
| [copywriters-handbook-skill](https://github.com/kangarooking/copywriters-handbook-skill) | 『The Copywriter's Handbook』 | 12 | 販売コピー・見出し・ベネフィット変換 |
| [contagious-skill](https://github.com/kangarooking/contagious-skill) | 『Contagious』 | 15 | STEPPS 伝播戦略と口コミ診断 |
| [influence-skill](https://github.com/kangarooking/influence-skill) | 『Influence』 | 12 | 説得心理と防御判断 |
| [1000-true-fans-skill](https://github.com/kangarooking/1000-true-fans-skill) | 『1000 True Fans』 | 13 | 個人ブランドと信頼ベース収益化 |
| [system-prompt-skills](https://github.com/kangarooking/system-prompt-skills) | 165個のAI製品システムプロンプト | 15 | システムプロンプト設計 |
| [X-growth-skills](https://github.com/kangarooking/X-growth-skills) | X（Twitter）実践資料集 | 15 | アカウント立ち上げ、コンテンツ、アルゴリズム、交流、収益化 |
| [poor-charlies-almanack-skill](https://github.com/kangarooking/poor-charlies-almanack-skill) | 『貧しきチャーリーの格言』 | 12 | マンガーの意思決定と判断法 |
| [no-rules-rules-skill](https://github.com/kangarooking/no-rules-rules-skill) | 『No Rules Rules』 | 10 | ネットフリックス式の組織設計 |
| [huangdi-neijing-skill](https://github.com/kangarooking/huangdi-neijing-skill) | 『黄帝内経』（素問+霊枢） | 22 | 思考方法（素問12+霊枢10） |
| [first-principles-skill](https://github.com/kangarooking/first-principles-skill) | 『第一性原理』 | 10 | 公理化思考と破界イノベーション |
| [mao-selected-works-skill](https://github.com/kangarooking/mao-selected-works-skill) | 『毛沢東選集』第1-5巻 | 25 | 認知・戦略・組織・実行の方法 |
| [qbdx-hub/buffett-letters-skill](https://github.com/qbdx-hub/buffett-letters-skill) | バフェット株主への手紙（1957-2023） | 20 | 投資と資本配分 |
| [qbdx-hub/wo-yu-di-tan-skill](https://github.com/qbdx-hub/wo-yu-di-tan-skill) | 『我与地坛』 | 6 | 制約・苦難・執筆・自己定位 |
| [qbdx-hub/mingchao-those-things-skill](https://github.com/qbdx-hub/mingchao-those-things-skill) | 『明朝那些事儿』 | 7 | 権力構造・制度失敗・歴史説明 |
| [qbdx-hub/sunzi-bingfa-skill](https://github.com/qbdx-hub/sunzi-bingfa-skill) | 『孫子兵法』 | 8 | 戦略判断・資源制御・行動選択 |
| [qbdx-hub/zhouyi-skill](https://github.com/qbdx-hub/zhouyi-skill) | 『周易』 | 8 | 状況診断・時機判断・進退境界 |
| [qbdx-hub/high-math-vol1-ch1-skill](https://github.com/qbdx-hub/high-math-vol1-ch1-skill) | 高等数学上冊第1章 | 8 | 極限・無限小・連続性の学習 |

## 動画蒸留ゾーン

これらのリポジトリは長編動画・コース・動画コレクションの字幕/書き起こしテキストから生成されたもので、cangjie-skill の非書籍コンテンツに対する方法論蒸留能力を示しています。

| リポジトリ | 元資料 | スキル数 |
|------------|--------|----------|
| [ai-for-everyone-skill](https://github.com/kangarooking/ai-for-everyone-skill) | アンドリュー・ン『AI for Everyone』動画コース | 25 |
| [loop-engineering-skill](https://github.com/kangarooking/loop-engineering-skill) | Loop Engineering 長編動画コレクション | 8 |

自分の蒸留リポジトリを上のリストに載せたい方は、[CONTRIBUTING.md](./CONTRIBUTING.md) の収録基準をご覧ください。

より多くの高価値な本の蒸留を計画中。候補には『君主論』などが含まれます。

追加の外部ソース（著者本人の許可を得て掲載）：

- 元リポジトリ: [ace3000chao/book2startup](https://github.com/ace3000chao/book2startup)
- 書目: 『リーン・スタートアップ』『孫子兵法』『荘子』『易経』
- 元リポジトリ: [shenqistart/book2skill](https://github.com/shenqistart/book2skill)
- 書目: 『纏論』『茶経』

## リポジトリ構造

```text
cangjie-skill/
├── README.md              ← 中国語版
├── README.en.md           ← 英語版
├── README.ja.md           ← 今見ているファイル
├── LICENSE                ← MIT
├── CONTRIBUTING.md        ← 貢献ガイド + スキルパック収録基準
├── SKILL.md               ← メタスキル定義（cangjie-skill の完全な実行仕様）
├── methodology/           ← RIA-TV++ の段階別方法論ドキュメント
├── extractors/            ← 5つの並行エクストラクターのプロンプト定義
├── templates/             ← SKILL.md / INDEX.md / BOOK_OVERVIEW.md テンプレート
├── scripts/               ← Star History チャート生成スクリプト
└── assets/                ← README で使用する画像
```

## エコシステム

cangjie-skill はより大きなスキルエコシステムの一部です：

- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — 人を蒸留する（思考スタイル、表現 DNA）
- **cangjie-skill**（このリポジトリ）— 本を蒸留する（方法論、フレームワーク、原則）
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — 任意のスキルを進化させる

これらは連携しています：nuwa は人を蒸留し、cangjie は本を蒸留し、darwin はそれらを進化させ続けます。

## コントリビューター

cangjie-skill エコシステムへの貢献に感謝します：

- [shenqistart](https://github.com/shenqistart) — 外部の [book2skill](https://github.com/shenqistart/book2skill) リファレンスを提供し、中英日 README を更新
- [qbdx-hub](https://github.com/qbdx-hub) — 6つの Cangjie 全書/章蒸留サンプルリポジトリを提供し、README リファレンスを更新

## 作者について

**袋鼠帝 kangarooking** — AI ブロガー、インディー開発者。AI Top 公式アカウント「袋鼠帝 AI 客栈」主宰

<img src="./assets/wechat-personal-qr.jpg" width="220" alt="袋鼠帝の個人 WeChat QR コード">

Volcengine ナビゲーション KOL、Baidu Qianfan 開発者アンバサダー、GLM エバンジェリスト、Trae 昆明初代 Fellow

| プラットフォーム | リンク |
|------------------|--------|
| 𝕏 Twitter | https://x.com/aikangarooking |
| 小紅書 | https://xhslink.com/m/5YejKvIDBbL |
| 抖音 | https://v.douyin.com/hYpsjphuuKc |
| WeChat 公式アカウント | 袋鼠帝 AI 客栈 |
| WeChat ビデオチャンネル | AI 袋鼠帝 |

WeChat 公式アカウント「袋鼠帝 AI 客栈」QR コード:

![](./assets/kangarooking-gzh.png)

本・長編動画・ポッドキャスト・コースの方法論を呼び出し可能な Agent Skills に一緒に蒸留したい方は、cangjie-skill WeCom グループへ：

<img src="./assets/wecom-cangjie-group-qr.png" width="220" alt="cangjie-skill WeCom グループ QR コード">

## ⭐ Star History

このプロジェクトが役に立ったら、スターをお願いします。

<a href="https://www.star-history.com/?repos=kangarooking%2Fcangjie-skill&type=date&legend=top-left">
 <img alt="Star History Chart" src="./assets/star-history.svg" />
</a>

## License

MIT. See [LICENSE](./LICENSE).
