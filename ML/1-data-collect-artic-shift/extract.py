import json
import csv

input_file_path = 'r_collegeresults_posts.jsonl'
output_file_path = 'output.csv'

with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Upvotes', 'Date', 'Title', 'Body Text', 'Link'])
    
    with open(input_file_path, 'rb') as jsonlfile:
        for line in jsonlfile:
            try:
                line = line.decode('utf-8', errors='ignore')
                
                post = json.loads(line)
                
                upvotes = post.get('ups', 0)
                date = post.get('created_utc', '')
                title = post.get('title', '')
                body_text = post.get('selftext', '')
                link = post.get('url', '')
                
                csv_writer.writerow([upvotes, date, title, body_text, link])
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON line: {line}")
