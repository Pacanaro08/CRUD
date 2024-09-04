import sqlite3


conn = sqlite3.connect("user-crud.db")


def create_table() -> None:
    """create the table if not exists"""
    
    conn.execute("""
    CREATE TABLE IF NOT EXISTS user (
        user_email TEXT PRIMARY KEY NOT NULL,
        user_password TEXT NOT NULL,
        user_name TEXT,
        user_phone INTEGER,
        user_address TEXT
    )
    """)

def create_user() -> None:
    pass


def update_user() -> None:
    pass


def delete_user() -> None:
    pass


def user_data() -> None:
    pass