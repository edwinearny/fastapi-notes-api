from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.db.models import Note
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse

router = APIRouter()


# ─── CREATE ───────────────────────────────────────────────
@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(
        title=note.title,
        content=note.content,
        is_important=note.is_important
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


# ─── LIST ALL ─────────────────────────────────────────────
@router.get("/", response_model=List[NoteResponse], status_code=200)
def list_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes


# ─── GET ONE ──────────────────────────────────────────────
@router.get("/{note_id}", response_model=NoteResponse, status_code=200)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


# ─── UPDATE ───────────────────────────────────────────────
@router.put("/{note_id}", response_model=NoteResponse, status_code=200)
def update_note(note_id: int, payload: NoteUpdate, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(note, field, value)

    db.commit()
    db.refresh(note)
    return note


# ─── DELETE ───────────────────────────────────────────────
@router.delete("/{note_id}", status_code=200)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return {"message": f"Note '{note.title}' deleted successfully"}
