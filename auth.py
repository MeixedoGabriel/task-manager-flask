from database import connect

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import re


def register_user(username, password):

    if not validate_password(password):
        return "weak_password"

    conn = connect()
    cursor = conn.cursor()

    password_hash = generate_password_hash(password)

    try:

        cursor.execute(
            """
            INSERT INTO users (
                username,
                password
            )
            VALUES (?, ?)
            """,
            (
                username,
                password_hash
            )
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login_user(username, password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:
        return None

    if check_password_hash(
        user[1],
        password
    ):
        return user[0]

    return None


def validate_password(password):

    # mínimo 6 caracteres
    if len(password) < 6:
        return False

    # pelo menos uma letra
    if not re.search(r"[A-Za-z]", password):
        return False

    # pelo menos um número
    if not re.search(r"\d", password):
        return False

    return True


def get_username(user_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return user[0]

    return ""