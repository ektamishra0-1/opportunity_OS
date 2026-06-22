import sqlite3

DB_NAME = "database/opportunity_os.db"


def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS observations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT NOT NULL,
        source_id TEXT UNIQUE,
        title TEXT,
        content TEXT,
        author TEXT,
        url TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_observation(observation):
    if observation_exists(observation.source_id):
        return  # skip duplicates

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO observations (
        source,
        source_id,
        title,
        content,
        author,
        url,
        timestamp
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        observation.source,
        observation.source_id,
        observation.title,
        observation.content,
        observation.author,
        observation.url,
        observation.timestamp
    ))

    conn.commit()
    conn.close()

def observation_exists(source_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM observations WHERE source_id = ?
    """, (source_id,))

    exists = cursor.fetchone() is not None
    conn.close()
    return exists