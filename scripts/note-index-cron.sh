#!/bin/bash
# note記事インデックス自動更新（cron用ラッパー）
# crontab: 0 9 * * * /mnt/c/src/cc-company/scripts/note-index-cron.sh >> /tmp/note-index.log 2>&1

set -e

export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"
export HOME="/home/kenji"
export LANG="ja_JP.UTF-8"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DATE=$(date +%Y-%m-%d)

echo "=== note-index-update: $LOG_DATE $(date +%H:%M:%S) ==="

cd "$PROJECT_DIR"
python3 scripts/note-index-update.py

echo "=== 完了: $(date +%H:%M:%S) ==="
