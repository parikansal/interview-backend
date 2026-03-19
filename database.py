from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://neondb_owner:npg_Iaujqoe3S4PE@ep-jolly-wildflower-ads2nsd5-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
