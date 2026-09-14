#!/usr/bin/env bash

# 定义常量
URL="http://127.0.0.1:8000/packages.json"
OUTPUT="summary.md"

# 写入 Markdown 标题和表头
echo "# API Package Report" > "$OUTPUT"
echo "" >> "$OUTPUT"
echo "| name | version | downloads |" >> "$OUTPUT"
echo "|------|---------|-----------|" >> "$OUTPUT"

# 使用 curl 获取数据，通过 jq 筛选、排序并格式化，追加到文件
curl -fsS "$URL" | jq -r '[.[] | select(.status == "active" and .downloads >= 100)] | sort_by([-.downloads, .name])[] | "| \(.name) | \(.version) | \(.downloads) |"' >> "$OUTPUT"

echo "报告已生成：$OUTPUT"
