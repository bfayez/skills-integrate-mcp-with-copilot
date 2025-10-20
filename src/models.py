from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class Signup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_email: str = Field(index=True)
    activity_name: str = Field(index=True)
    signed_at: datetime = Field(default_factory=datetime.utcnow)


class Activity(SQLModel, table=True):
    name: str = Field(primary_key=True)
    description: Optional[str] = None
    schedule: Optional[str] = None
    max_participants: Optional[int] = None


class User(SQLModel, table=True):
    email: str = Field(primary_key=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
