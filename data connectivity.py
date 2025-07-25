import sqlite3
conn = sqlite3.connect("my_database.db")
print("✅ Connected to SQLite database")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 22))
conn.commit()
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("📋 Students table:")
for row in rows:
    print(row)
conn.close()
print("🔒 SQLite connection closed")
