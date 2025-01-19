from fastapi import FastAPI, status, Depends
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .schemas import PostCreate, PostBaseResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()    
    
# Welcome at root url
@app.get("/")
def root():
    return {"message": "Welcome to my API now go to /docs to see the documentation"}

# Getting all posts
@app.get("/posts/")
def get_posts(db: Session = Depends(get_db)):
    all_posts = db.query(models.Post).all()
    if len(all_posts) == 0:
        return {
            "message": "No posts found. Try creating one.",
            "status": status.HTTP_404_NOT_FOUND
            }
    return all_posts


# Getting an indiviual post
@app.get("/posts/{id}/", status_code=status.HTTP_200_OK)
def get_post(id: int, db: Session = Depends(get_db)):
    single_post =  db.query(models.Post).filter(models.Post.id == id).first()
    if single_post is None:
        return {
            "message": f"post with id: {id} doesn't exist. Try another.",
            "status": status.HTTP_404_NOT_FOUND
            }
    return single_post


# Creating a post 
@app.post("/posts/",status_code=status.HTTP_201_CREATED,response_model=PostBaseResponse)
def create_posts(post: PostCreate, db: Session = Depends(get_db)):
    # creating new post instance
    created_post = models.Post(**post.dict())
    
    # Adding the new instance to the database
    db.add(created_post)
    
    # commit the changes to the database
    db.commit()
    db.refresh(created_post)
    return created_post


# Updating indiviual post
@app.put("/posts/{id}/", status_code=status.HTTP_200_OK)
def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    
    # Find the intended post 
    post_instance = db.query(models.Post).filter(models.Post.id == id).first()
    
    # check if it exist in the DB
    if post_instance is None:
        return {
            "message":f"post with id: {id} doesn't exist. Try another.",
            "status": status.HTTP_404_NOT_FOUND
        }
    
    # create the update post object 
    for key, value in post.dict().items():
        setattr(post_instance,key,value)
    
    db.commit()
    
    return post_instance


# delete an indiviual post
@app.delete("/posts/{id}/",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # Capture the intended post entry
    post_to_delete = db.query(models.Post).filter(models.Post.id == id).first()
    
    # check if the post exist
    if post_to_delete is None: 
        return {
            "message":f"post with id: {id} doesn't exist. Try another.",
            "status": status.HTTP_404_NOT_FOUND
        }
    # delete that post 
    db.delete(post_to_delete)
    db.commit()
    return {"message": "Successfully Deleted"}
