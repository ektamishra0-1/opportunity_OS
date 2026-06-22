from database.db import get_connection


def view_observations(limit=20):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT source, title, author, url, timestamp
        FROM observations
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    for row in rows:
        print("\n---")
        print(f"SOURCE: {row[0]}")
        print(f"TITLE: {row[1]}")
        print(f"AUTHOR: {row[2]}")
        print(f"URL: {row[3]}")
        print(f"TIME: {row[4]}")

    conn.close()


if __name__ == "__main__":
    view_observations()