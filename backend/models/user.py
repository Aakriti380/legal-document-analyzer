from pydantic import BaseModel,EmailStr

class UserRegeister(BaseModel):
    name:str
    email:EmailStr
    password:str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str