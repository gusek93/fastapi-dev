from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String, Boolean, DateTime, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings


engine = create_engine(
    settings.database_url
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('email', String(50), unique=True, index=True),
    Column('hashed_password', String(255)),
    Column('is_active', Boolean, default=True),
    Column('deleted_at', DateTime),
)

items = Table(
    'items', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('title', String(20), index=True),
    Column('description', String(100), index=True),
    Column('deleted_at', DateTime),
    Column('owner_id', Integer, ForeignKey("users.id")),
)

meta.create_all(engine)