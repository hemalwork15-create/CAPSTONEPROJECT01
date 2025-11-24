from pydantic import BaseModel
from typing import Optional

class DocumentCreate(BaseModel):
    title: str
    category_id: int
    uploader_id: int

class DocumentOut(BaseModel):
    id: int
    title: str
    category_id: int
    file_path: str
    uploader_id: int

    class Config:
        orm_mode = True
