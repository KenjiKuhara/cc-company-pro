#!/bin/bash
# note記事インデックス自動更新（cron用ラッパー）
# crontab: 0 9 * * * /path/to/cc-company-pro/scripts/note-index-cron.sh /path/to/your/project >> /tmp/note-index.log 2>&1
# 第1引数: .company/ があるプロジェクトディレクトリ

set -e

export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
export LANG="C.UTF-8"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="${1:-$(dirname "$SCRIPT_DIR")}"
LOG_DATE=$(date +%Y-%m-%d)

echo "=== note-index-update: $LOG_DATE $(date +%H:%M:%S) ==="

cd "$PROJECT_DIR"
python3 "$SCRIPT_DIR/note-index-update.py"

echo "=== 完了: $(date +%H:%M:%S) ==="
