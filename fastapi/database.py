from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "beyza"
password = "beyza1234"
host = "127.0.0.1"
port = "5432"
name = "cognitus"
uri = "postgresql://{}:{}@{}:{}/{}".format(
    user, password, host, port, name
)
engine = create_engine(uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()