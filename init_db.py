import contextlib
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Lähde: https://docs.sqlalchemy.org/en/20/core/engines.html
engine = create_engine(f"postgresql://{os.getenv('DB_USER')}"
                       f":{os.getenv('DB_PASSWORD')}"
                       f"@{os.getenv('DB_SERVICE_NAME')}"
                       f"/{os.getenv('DB_NAME')}")

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
