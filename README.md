# Tech Job Trends Tracker
A Python project to scrape tech job listings from Wellfound (AngelList), store them in a PostgreSQL database, and prepare data for analysis and visualization.
## Features

- Scrapes job title, company, location, and salary data from software engineer listings
- Saves scraped data into a PostgreSQL database
- Modular and scalable code structure for easy enhancements (pagination, skill extraction, visualization)
- Configuration via environment variables for secure credential management

---

## Folder Structure
```text
tech_job_tracker/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── db/
│   ├── __init__.py
│   ├── init_db.py
│   └── db_utils.py
│
├── scraper/
│   ├── __init__.py
│   ├── job_scraper.py
│   └── parsers.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── analysis/
│   ├── __init__.py
│   └── visualize.py
│
├── scripts/
│   └── run_scraper.py
│
├── .env
├── requirements.txt
└── README.md

```

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- PostgreSQL database instance

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/aaronGeb/tech_job_tracker.git
   cd tech_job_tracker

2. **Create and configure PostgreSQL database**
    ```
    createdb jobs_db
    ```



3. **Set up environment variables**
    ```
    POSTGRES_DB=jobs_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```

4. **Install dependencies**
   
    Use UV to install project dependencies:
    ```
    uv install
    ```

# Running the Scraper
Run the main script to initialize the database and scrape job listings:
    ```
    python scripts/run_scraper.py
    ```






# License
MIT [LICENSE](../tech_job_tracker/LICENSE) © 2025 Aaron.

# Contact
Feel free to open issues or submit pull requests.
You can reach me at [Email](aarongebremariam.94@gmail.com)