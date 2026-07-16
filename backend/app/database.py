import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    postgres_user = os.getenv("POSTGRES_USER")
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_host = os.getenv("POSTGRES_HOST", "localhost")
    postgres_port = os.getenv("POSTGRES_PORT", "5432")
    postgres_db = os.getenv("POSTGRES_DB")

    if not postgres_user or not postgres_password or not postgres_db:
        raise RuntimeError(
            "Set DATABASE_URL or POSTGRES_USER/POSTGRES_PASSWORD/POSTGRES_DB environment variables."
        )

    return (
        f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:"
        f"{postgres_port}/{postgres_db}"
    )


# db url used to connect to Postgres
DATABASE_URL = get_database_url()

# Creates SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# SessionLocal class created for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models inherit from base class
Base = declarative_base()

# Dependency to get database session per request
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

