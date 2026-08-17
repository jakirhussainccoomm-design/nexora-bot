import sqlite3

DB_NAME = "nexora.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            earn_balance REAL DEFAULT 0,
            deposit_balance REAL DEFAULT 0,
            pending_withdrawal REAL DEFAULT 0,
            lifetime_earned REAL DEFAULT 0,
            referral_income REAL DEFAULT 0,
            completed_tasks INTEGER DEFAULT 0,
            in_review INTEGER DEFAULT 0,
            rejected INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def create_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (user_id,)
    )

    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            earn_balance,
            deposit_balance,
            pending_withdrawal,
            lifetime_earned,
            referral_income,
            completed_tasks,
            in_review,
            rejected
        FROM users
        WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()

    conn.close()

    return result
