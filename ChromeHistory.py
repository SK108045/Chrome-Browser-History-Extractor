import sqlite3

# Specify the path to your Chrome History file
# Replace this with the actual path on your system
history_path = r"path/to/your/Chrome/History/file"

# Specify the output file path
output_file_path = r"browsing_history.txt"

# Connect to the SQLite database
conn = sqlite3.connect(history_path)
cursor = conn.cursor()

# SQL query to select browsing history
query = """
SELECT id, url, title, visit_count, typed_count, last_visit_time, hidden
FROM urls
"""

# Execute the query
cursor.execute(query)

# Fetch all results
history_items = cursor.fetchall()

# Open the output file and write the browsing history
with open(output_file_path, 'w', encoding='utf-8') as file:
    for item in history_items:
        id, url, title, visit_count, typed_count, last_visit_time, hidden = item
        file.write(f"ID: {id}\nURL: {url}\nTitle: {title}\nVisit Count: {visit_count}\n")
        file.write(f"Typed Count: {typed_count}\nLast Visit Time: {last_visit_time}\nHidden: {hidden}\n\n")

# Close the database connection
conn.close()

print(f"Browsing history has been saved to {output_file_path}")
