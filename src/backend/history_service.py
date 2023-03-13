from .models import conn ,c
import datetime
import sqlite3
import os

def save_to_history(title, file_name):
    # Save the downloaded file to the history in the database
    download_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO downloaded_files (title, file_name, download_date) VALUES (?, ?, ?)',
              (title, file_name, download_date))
    conn.commit()

def get_history():
    # Retrieve all downloaded files from the database
    c.execute('SELECT * FROM downloaded_files')
    rows = c.fetchall()

    # Format the downloaded files as a list of dictionaries
    downloaded_files = []
    for row in rows:
        file_dict = {'id': row[0], 'title': row[1], 'file_name': row[2], 'download_date': row[3]}
        downloaded_files.append(file_dict)

    return downloaded_files

def clear_history():
    # Connect to the downloads database
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    db_path = os.path.join(project_root, 'downloads.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Delete all rows from the downloaded_files table
    c.execute('DELETE FROM downloaded_files')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print('Download history cleared.')


def delete_from_history(file_name):
    # Connect to the downloads database
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    db_path = os.path.join(project_root, 'downloads.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Delete the row(s) with the matching file_name from the downloaded_files table
    c.execute('DELETE FROM downloaded_files WHERE file_name = ?', (file_name,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f'{file_name} deleted from download history.')