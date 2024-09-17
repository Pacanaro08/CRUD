import sqlite3


def create_table() -> None:
    """create the table if not exists"""
    
    try:
        conn = sqlite3.connect('user-crud.db')
        conn.execute("""
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT
            user_email TEXT NOT NULL,
            user_password TEXT NOT NULL,
            user_name TEXT,
            user_phone INTEGER,
            user_address TEXT
        )
        """)
    except:
        print("create'nt")

def create_user(user_data:dict) -> None:
    """create new user"""

    try:
        conn = sqlite3.connect('user-crud.db')
        cursor = conn.cursor()

        query = """INSERT INTO user (user_email, user_password, user_name, user_phone, user_address)
         VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (
            user_data.get('email'), 
            user_data.get('password'), 
            user_data.get('name'), 
            user_data.get('phone'), 
            user_data.get('address')
        ))

        conn.commit()
        return 'Success!'
    
    except sqlite3.IntegrityError as error:
        return error
    
    finally:
        conn.close()


def update_user(user_data:dict) -> None:
    """update user based on id"""

    try:
        conn = sqlite3.connect('user-crud.db')
        cursor = conn.cursor()

        query = """UPDATE user SET user_email = ?, user_password = ?, user_name = ?, user_phone = ?,
        user address = ? WHERE user_id = ?"""
        cursor.execute(query, (
            user_data.get('email'), 
            user_data.get('password'), 
            user_data.get('name'), 
            user_data.get('phone'), 
            user_data.get('address'),
            user_data.get('id')
        ))

        conn.commit()
        return 'Success!'

    except sqlite3.IntegrityError as error:
        return error

    finally:
        conn.close()


def delete_user(user_id:int) -> None:
    """delete user based on id"""

    try:
        conn = sqlite3.connect('user-crud.db')
        cursor = conn.cursor()

        query = """DELETE user WHERE user_id = ?"""
        cursor.execute(query, (user_id))

        conn.commit()
        return 'Success!'

    except sqlite3.IntegrityError as error:
        return error

    finally:
        conn.close()


def user_data(user_email:str, user_password:str) -> None:
    """get user info based on email and password"""

    conn = sqlite3.connect('user-crud.db')
    cursor = conn.cursor()

    query = """SELECT * FROM user WHERE user_email = ? AND user_password = ?"""
    cursor.execute(query, (user_email, user_password))

    result = cursor.fetchone()

    if result is None:
        return{}
    
    column_names = [description[0] for description in cursor.description]

    user_info = dict(zip(column_names, result))

    conn.close()
    return user_info


def verify_email_existance(user_email:str) -> None:
    """see if the e-mail already exists in database"""

    conn = sqlite3.connect('user-crud.db')
    cursor = conn.cursor()

    query = """SELECT * FROM user WHERE user_email = ?"""
    cursor.execute(query, (user_email))

    result = cursor.fetchone()

    conn.close()
    return None if result is None else 'E-mail already exists!'