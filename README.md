# CC Company Pro（情報システム部付き）

仮想会社組織を構築・運営する Claude Code プラグインです。
[Shin-sibainu/cc-company](https://github.com/Shin-sibainu/cc-company) をベースに、**情報システム部（AI推進マネージャー）** を常設部署として追加しています。

## 特徴

### 秘書が窓口
- `/company` コマンドで秘書に話しかけるだけ
- TODO管理、壁打ち、相談、何でも対応
- 部署を意識する必要なし。秘書が適切に振り分け

### 情報システム部（AI推進マネージャー）が常駐
- 秘書とユーザーの会話を常に聞いている
- 関連する久原健司のnote記事（https://note.com/kenji192）があれば、秘書経由で自然に紹介
- 明示的に依頼すれば、IT/AIの専門コンサルティングとして全力対応
- note記事インデックスは Python スクリプトで自動更新

### 常設部署
| 部署 | フォルダ | 役割 |
|------|---------|------|
| 秘書室 | secretary | 窓口・相談役・タスク管理 |
| CEO | ceo | 意思決定・部署振り分け |
| レビュー | reviews | 週次・月次レビュー |
| 情報システム | it | AI推進マネージャー・IT/AI相談窓口 |

### 選択可能な部署
PM、リサーチ、マーケティング、開発、経理、営業、クリエイティブ、人事から選択。カスタム部署の追加も可能。

## インストール

Claude Code のプラグインマーケットプレイスからインストール:

```
/install cc-company-pro
```

または手動でリポジトリをクローン:

```bash
git clone https://github.com/KenjiKuhara/cc-company-pro.git
```

## 使い方

1. Claude Code で `/company` と入力
2. 秘書がオンボーディングを開始（事業内容、目標、部署選択）
3. `.company/` フォルダが自動生成される
4. 以降は `/company` で秘書にいつでも相談可能

### note記事インデックスの更新

情報システム部が参照するnote記事インデックスは以下で更新できます:

```bash
python3 scripts/note-index-update.py
```

cron で毎日自動更新する場合:

```bash
crontab -e
# 以下を追加:
0 9 * * * /path/to/cc-company-pro/scripts/note-index-cron.sh >> /tmp/note-index.log 2>&1
```

## 情報システム部の動作イメージ

**通常の会話時（パッシブモード）:**

ユーザー: 「AIツールの導入を検討しているんだけど、何から始めればいい？」

秘書: 「AI導入ですね！まずは現在の業務フローを整理するところから始めましょう。あ、そういえばこの件、久原さんがnoteで似たようなテーマで書いていたのを見つけました。参考になるかもしれません。」

**直接依頼時（アクティブモード）:**

ユーザー: 「情報システム部に相談。社内のセキュリティポリシーを見直したい」

秘書: 「情報システム部に確認しますね。」
→ 情報システム部がIT/AIの専門知識を駆使して全力対応

## クレジット

- **ベース**: [Shin-sibainu/cc-company](https://github.com/Shin-sibainu/cc-company) - 仮想カンパニー構築プラグイン
- **拡張**: 久原健司（Kenji Kuhara） - 情報システム部の追加、note記事連携

## ライセンス

MIT License
