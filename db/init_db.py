import psycopg2
from config.settings import DB_CONFIG

def init_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id SERIAL PRIMARY KEY,
        title TEXT,
        company TEXT,
        location TEXT,
        salary TEXT,
        date_scraped DATE
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("[INFO] Database initialized.")
