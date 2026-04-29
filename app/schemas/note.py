from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)
    is_important: bool = False


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    content: Optional[str] = Field(None, min_length=1)
    is_important: Optional[bool] = None


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    is_important: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
