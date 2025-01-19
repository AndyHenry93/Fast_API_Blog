from pydantic import BaseModel

class PostBaseRequest(BaseModel):
    title: str
    content: str
    published: bool = False
    
    class Config:
        from_attributes = True
        
        
class PostBaseResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    
    class Config:
        from_attributes = True
        
class PostCreate(PostBaseRequest):
    pass
