if [ $# -ne 1 ]; then
	echo "Usage: $0 <csv-file>" >&2
	exit 1
fi

csv_file="$1"

if [ ! -f "$csv_file" ]; then
	echo "Error: File '$csv_file' not found" >&2
	exit 1
fi

echo "Top 2 5xx paths:"
grep -v '^timestamp' "$csv_file" \
    | awk -F, '$4 >= 500 && $4 < 600 {print $3}' \
    | sort \
    | uniq -c \
    | sort -k1,1nr -k2,2 \
    | head -2 \
    | awk '{print $2, $1}'

avg=$(awk -F, 'NR > 1 {sum += $5; count++} END {if (count) printf "%.2f", sum/count; else print "0"}' "$csv_file")
echo "Average latency: $avg ms"
