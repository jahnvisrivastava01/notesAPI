from fastapi import FastAPI
from database import engine
import models
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Notes API is running!"}


@app.post("/notes", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate):
    db = SessionLocal()

    new_note=models.Note(
        title=note.title,
        content=note.content
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

@app.get("/notes", response_model=list[schemas.Note])
def get_notes():
    db = SessionLocal()

    notes = db.query(models.Note).all()

    return notes

@app.put("/notes/{id}", response_model=schemas.Note)
def update_note(id: int, updated_note: schemas.NoteCreate):
    db = SessionLocal()

    note = db.query(models.Note).filter(models.Note.id == id).first()

    note.title = updated_note.title
    note.content = updated_note.content

    db.commit()
    db.refresh(note)

    return note


@app.delete("/notes/{id}")
def delete_note(id: int):
    db = SessionLocal()

    note = db.query(models.Note).filter(models.Note.id == id).first()

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}