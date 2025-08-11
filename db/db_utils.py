import psycopg2
from psycopg2.extras import execute_values
from config.settings import DB_CONFIG

def save_jobs(jobs):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    insert_query = """
        INSERT INTO jobs (title, company, location, salary, date_scraped)
        VALUES %s
    """
    job_values = [(job["title"], job["company"], job["location"], job["salary"], job["date_scraped"]) for job in jobs]
    execute_values(cur, insert_query, job_values)
    conn.commit()
    conn.close()
    print(f"[INFO] Saved {len(jobs)} jobs to database.")
