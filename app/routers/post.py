from fastapi import FastAPI, Response, status ,HTTPException, Depends, APIRouter
from .. import models, schemas
from sqlalchemy.orm import Session 
from ..database import SessionLocal, engine, get_db
from typing import Optional, List  

router = APIRouter(
    prefix = "/posts",
    tags = ["Posts"]
)


# Retreive all the posts  
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return posts 


    # cursor.execute(""" SELECT * FROM posts """)
    # posts = cursor.fetchall()
    # return{"data": posts}
 
# Create a post 
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # Same as RETURNING * in Raw SQL 

    return new_post



    # cursor.execute("""  
    #                INSERT INTO posts (title, content, published) 
    #                VALUES (%s, %s, %s) RETURNING * """,
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    # return {"data": new_post}


# Retreive a specific post by id 
@router.get("/{id}", response_model=schemas.Post)  # here id = path parameter 
def get_post(id: int, db: Session = Depends(get_db)):
    
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} was not found")
    
    return post 

# Delete a post 
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    deleted_post = db.query(models.Post).filter(models.Post.id == id)

    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} not found")
    
    deleted_post.delete(synchronize_session=False)

    db.commit()
    
    return {"message": "Post deleted successfully"} # here deleted_post = delete_post


    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    # deleted_post = cursor.fetchone()

    # if deleted_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail= f"post with id: {id} not found")
    # conn.commit()
    # return {"message": "Post deleted successfully"} # here deleted_post = delete_post


# Update a post 

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first() 

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with id: {id} not found")

    post_query.update(updated_post.dict(), synchronize_session=False)  # type: ignore

    db.commit()
    
    return post_query.first() 

    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, 
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    # return {"data": updated_post}

