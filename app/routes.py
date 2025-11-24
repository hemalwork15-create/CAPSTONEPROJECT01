from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import os
from . import crud, models, schemas
from .database import get_db

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/documents/", response_model=schemas.DocumentOut)

async def upload_document(title: str, category_id: int, uploader_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    doc = schemas.DocumentCreate(title=title, category_id=category_id, uploader_id=uploader_id)
    return crud.create_document(db, doc, file_path)

@router.get("/documents/", response_model=list[schemas.DocumentOut])
def list_documents(db: Session = Depends(get_db)):
    return crud.get_documents(db)
