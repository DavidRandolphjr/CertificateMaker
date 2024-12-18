import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("saved_entries.db")
cursor = conn.cursor()

# Use pandas to read the table directly into a DataFrame
df = pd.read_sql_query("SELECT * FROM entries", conn)

# Adjust the display settings to avoid truncation
pd.set_option('display.max_colwidth', None)  # No truncation of column contents
pd.set_option('display.max_columns', None)   # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping to new lines

# Print the DataFrame (which includes the headers)
# print(df)
# cursor.execute("DELETE FROM entries WHERE cert_name = 'tim' AND date_issued = 'asdf'")
# conn.commit()
fd = pd.read_sql_query("SELECT * FROM entries WHERE cert_name = 'tim'", conn)

# Iterate over each row in the DataFrame
for index, row in fd.iterrows():
    print(f"Row {index + 1}:")
    # For each column, print the header and corresponding value
    for header in fd.columns:
        print(f"{header}: {row[header]}")
    print("-" * 40)  # Separator between rows

for i in fd:
    print("value: ", i.columns)

# print(fd.to_string())

# Close the connection
conn.close()
