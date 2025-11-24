from fastapi import FastAPI, UploadFile, File, Form, Depends
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
import os

from . import crud, models
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

templates = Jinja2Templates(directory="app/templates")

# Render upload page
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Handle form upload
@app.post("/upload/")
async def upload_document(
    request: Request,
    title: str = Form(...),
    category_id: int = Form(...),
    uploader_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    crud.create_document(db, models.Document(title=title, category_id=category_id, uploader_id=uploader_id, file_path=file_path), file_path)
    return templates.TemplateResponse("index.html", {"request": request, "message": "Upload successful!"})

# List all documents
@app.get("/documents/")
def list_documents(request: Request, db: Session = Depends(get_db)):
    documents = crud.get_documents(db)
    return templates.TemplateResponse("list.html", {"request": request, "documents": documents})

# Download file
@app.get("/download/{doc_id}")
def download_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Document).filter(models.Document.id == doc_id).first()
    if doc and os.path.exists(doc.file_path):
        return FileResponse(doc.file_path, filename=os.path.basename(doc.file_path))
    return {"error": "File not found"}
