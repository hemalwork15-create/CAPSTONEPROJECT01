from sqlalchemy.orm import Session
from . import models, schemas

def create_document(db: Session, doc: schemas.DocumentCreate, file_path: str):
    db_doc = models.Document(
        title=doc.title,
        category_id=doc.category_id,
        uploader_id=doc.uploader_id,
        file_path=file_path
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def get_documents(db: Session):
    return db.query(models.Document).all()
