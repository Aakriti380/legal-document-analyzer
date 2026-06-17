from pydantic import BaseModel

class DocumentModel(BaseModel):
    filename:str
    document_type:str