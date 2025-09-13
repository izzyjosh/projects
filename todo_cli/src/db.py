from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
  pass
  
  
def get_db():
  db = SessionLocal()
  try:
    yield db
  except Exceptions as e:
    raise e
  finally:
    db.close()