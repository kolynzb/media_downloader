import os
import sqlite3

# Get the absolute path of the root folder of your project
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect(os.path.join(project_root, 'downloads.db'))

c = conn.cursor()

# Create the table to store downloaded files if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS downloaded_files 
             (id INTEGER PRIMARY KEY, title TEXT, file_name TEXT, download_date TEXT)''')
