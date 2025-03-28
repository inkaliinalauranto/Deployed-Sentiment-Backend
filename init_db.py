import contextlib
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f"sqlite:///{os.getenv('DB_NAME')}.db?check_same_thread=False")
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextlib.contextmanager
def init_db_conn():
    conn = None
    try:
        conn = session()
        yield conn
    finally:
        if conn is not None:
            conn.close()
