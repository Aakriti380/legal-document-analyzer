from pydantic import BaseModel

class ChatModel(BaseModel):
    question: str
    
'''Pydantic schemas provide automatic request validation, type checking, data parsing, and clear API documentation. They ensure that only correctly structured data reaches the business logic layer.'''