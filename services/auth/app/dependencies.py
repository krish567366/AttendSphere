# This file will contain FastAPI dependency functions.
# For example, getting the current user, database session, etc.

# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
# from . import crud, models, schemas, main, config
# from jose import JWTError, jwt

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # Assuming /token will be the login endpoint

# def get_db():
#     db = main.SessionLocal() # Assuming SessionLocal is defined in main.py or db_setup.py
#     try:
#         yield db
#     finally:
#         db.close()

# async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = schemas.TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = crud.get_user_by_email(db, email=token_data.username) # Assuming get_user_by_email exists
#     if user is None:
#         raise credentials_exception
#     return user
