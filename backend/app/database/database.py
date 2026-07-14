from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# db url used to connect to Postgres
DATABASE_URL = ""

# Creates SQLAlchemy engine
engine = create_engine(DATABASE_URL)

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

