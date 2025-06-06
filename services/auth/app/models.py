from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # roles = relationship("Role", secondary="user_roles") # Placeholder for UserRole association

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    permissions = Column(JSON, nullable=True) # e.g., ["read_users", "write_users"]
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Placeholder for UserRole association table
# class UserRole(Base):
#     __tablename__ = "user_roles"
#     user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
#     role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
