OUTPUT_FILENAME=bash_result.txt

unique_requests_count=$(cat "$1" | awk '{print $6, $7, $8}' | sort -u | wc -l)
echo UNIQUE REQUESTS > "$OUTPUT_FILENAME"
echo "$unique_requests_count" >> "$OUTPUT_FILENAME"
echo >> "$OUTPUT_FILENAME"

echo REQUESTS STATS >> "$OUTPUT_FILENAME"
cat "$1" | awk '{print $6, $7, $8}' | sort -u | awk '{print substr($1, 2)}'  | uniq -c >> "$OUTPUT_FILENAME"
echo >> "$OUTPUT_FILENAME"

echo TOP 10 MOST FREQUENT >> "$OUTPUT_FILENAME"
cat "$1" | awk '{print $6, $7, $8}' | sort | uniq -c | sort -rnk 1 | head -n 10 | awk '{print $1, $3}' >> "$OUTPUT_FILENAME"
echo >> "$OUTPUT_FILENAME"

echo TOP 5 REQUEST BY BODY BYTES SENT WITH 4XX STATUS CODE >> "$OUTPUT_FILENAME"
cat "$1" | awk '{print $1,$9,$10,$7}' | awk '$2~/^4/' | sort -rk 3 | head -n 5 >> "$OUTPUT_FILENAME"
echo >> "$OUTPUT_FILENAME"

echo TOP 5 USERS BY REQUESTS COUNT WITH 5XX STATUS CODE >> "$OUTPUT_FILENAME"
cat "$1" | awk '{print $1, $9}' | sort | uniq -c | awk '$3 ~ /^5/' | sort -rnk 1 | head -n 5 | awk '{print $1, $2}' >> "$OUTPUT_FILENAME"