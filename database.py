import sqlite3
import datetime

DB_NAME= "history.db"

def init_db():
    conn=sqlite3.connect(DB_NAME)
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                command TEXT,
                input TEXT,
                result TEXT,
                timestamp TEXT)
                ''')
    conn.commit()
    conn.close()

def add_record(user_id, command, input_data, result):
    conn=sqlite3.connect(DB_NAME)
    c = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    c.execute("INSERT INTO history (user_id, command, input, result, timestamp) VALUES (?, ?, ?, ?, ?)",
        (user_id, command, input_data, result, timestamp))
    conn.commit()
    conn.close()

def get_history(user_id, limit=10):
    conn = sqlite3.connect(DB_NAME)
    c= conn.cursor()
    c.execute("SELECT command, input, result, timestamp FROM history WHERE user_id = ? ORDER BY time stamp DESC LIMIT ?",
              (user_id, limit))
    rows = c.fetchall()
    conn.close()
    return rows
