from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create SQLite engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./juri.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Juri API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Juri API"}

# Include routers (we'll create these next)
# from routers import articles, comments, users
# app.include_router(articles.router)
# app.include_router(comments.router)
# app.include_router(users.router)