#!/usr/bin/env python3
"""
久原健司のnote記事URL一覧を自動取得し、インデックスファイルを更新するスクリプト。
CC Company情報システム部のAI推進マネージャーが参照する情報源。

Usage:
    python3 scripts/note-index-update.py

Output:
    .company/it/note-article-index.md
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

NOTE_USERNAME = "kenji192"
API_BASE = f"https://note.com/api/v2/creators/{NOTE_USERNAME}/contents"
OUTPUT_PATH = Path.cwd() / ".company" / "it" / "note-article-index.md"

JST = timezone(timedelta(hours=9))


def fetch_all_articles():
    """noteのAPIから全記事を取得する"""
    articles = []
    page = 1

    while True:
        url = f"{API_BASE}?kind=note&page={page}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "CC-Company-NoteIndexer/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.URLError as e:
            print(f"Error fetching page {page}: {e}")
            break

        contents = data.get("data", {}).get("contents", [])
        if not contents:
            break

        for article in contents:
            articles.append({
                "title": article.get("name", ""),
                "url": article.get("noteUrl", ""),
                "published": article.get("publishAt", ""),
                "likes": article.get("likeCount", 0),
                "price": article.get("price", 0),
            })

        is_last = data.get("data", {}).get("isLastPage", True)
        if is_last:
            break

        page += 1

    return articles


def generate_markdown(articles):
    """記事一覧をMarkdown形式で出力する"""
    now = datetime.now(JST).strftime("%Y-%m-%d %H:%M")
    total = len(articles)

    lines = [
        "# note記事インデックス（自動生成）",
        "",
        f"> **最終更新**: {now}",
        f"> **総記事数**: {total}件",
        f"> **著者**: 久原健司（kenji192）",
        f"> **プロフィール**: https://note.com/{NOTE_USERNAME}",
        "> **更新方法**: `python3 scripts/note-index-update.py` または cron で自動実行",
        "",
        "---",
        "",
        "## 記事一覧（新しい順）",
        "",
    ]

    for i, a in enumerate(articles, 1):
        pub_date = ""
        if a["published"]:
            try:
                dt = datetime.fromisoformat(a["published"].replace("Z", "+00:00"))
                pub_date = dt.astimezone(JST).strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                pub_date = a["published"][:10] if len(a["published"]) >= 10 else ""

        price_tag = " [有料]" if a["price"] and a["price"] > 0 else ""
        lines.append(f"{i}. [{a['title']}]({a['url']}) ({pub_date}){price_tag}")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## AI推進マネージャー向け検索ガイド")
    lines.append("")
    lines.append("このファイルは情報システム部のAI推進マネージャーが、ユーザーからのAI関連の相談に対して")
    lines.append("久原さんのnote記事を優先的に参照するための情報源です。")
    lines.append("")
    lines.append("### 検索の優先順位")
    lines.append("1. **まずこのインデックスからタイトルで関連記事を探す**")
    lines.append("2. 該当する記事があれば、WebFetchで記事本文を読み、要点を紹介する")
    lines.append("3. 該当する記事がない場合のみ、一般のWeb検索にフォールバックする")

    return "\n".join(lines)


def main():
    print(f"note記事インデックスを更新中... ({NOTE_USERNAME})")

    articles = fetch_all_articles()
    if not articles:
        print("記事が取得できませんでした。")
        return 1

    print(f"  {len(articles)}件の記事を取得しました。")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    md = generate_markdown(articles)
    OUTPUT_PATH.write_text(md, encoding="utf-8")
    print(f"  インデックスを更新しました: {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    exit(main())
