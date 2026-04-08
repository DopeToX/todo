import uuid
from datetime import datetime, timedelta
from db import get_cursor

def create_token(user_id: int):
    token = str(uuid.uuid4())
    now = datetime.utcnow()
    exp = now + timedelta(hours=1)

    cur = get_cursor()

    try:
        cur.execute("""
            INSERT INTO tokens (user_id, token, created_at, expires_at)
            VALUES (%s, %s, %s, %s)
        """, (user_id, token, now, exp))

        cur.connection.commit()
        return token

    except Exception as e:
        cur.connection.rollback()
        raise e


def check_token(token: str):
    cur = get_cursor()
    cur.execute("""
        SELECT * FROM tokens
        WHERE token=%s AND expires_at > NOW()
    """, (token,))
    return cur.fetchone()