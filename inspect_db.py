import sqlite3
conn = sqlite3.connect('reports/safety_analytics.db')
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('Tables:', [t[0] for t in tables])
for t in tables:
    cols = conn.execute(f"PRAGMA table_info({t[0]})").fetchall()
    print(f"\n{t[0]}:", [(c[1], c[2]) for c in cols])
    sample = conn.execute(f"SELECT * FROM {t[0]} LIMIT 2").fetchall()
    print("Sample:", sample)
