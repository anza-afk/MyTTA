
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, DateTime
from sqlalchemy.orm import relationship

from .database import Base


superuser_ticket = Table(
    "superuser_ticket",
    Base.metadata,
    Column(
        "superuser_id",
        ForeignKey("superusers.id"),
        primary_key=True,
        nullable=True),
    Column("ticket_id", ForeignKey("tickets.id"), primary_key=True),
)

profile_department = Table(
    "profile_department",
    Base.metadata,
    Column("profile_id", ForeignKey("profiles.id"), primary_key=True),
    Column("department_id", ForeignKey("departments.id"), primary_key=True),
)

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime)
    resolved_at = Column(DateTime, nullable=True)
    creator_id = Column(Integer, ForeignKey("users.id"))
    superuser = relationship("Superuser", secondary=superuser_ticket, back_populates="tickets")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    profile = relationship("Profile", back_populates="user", uselist=False)
    tickets = relationship("Ticket", backref='user')


class Superuser(Base):
    __tablename__ = "superusers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    tickets = relationship("Ticket", secondary=superuser_ticket, back_populates="superuser")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    surname = Column(String, index=True)
    name = Column(String, index=True)
    patronymic = Column(String, index=True)

    departments = relationship('Department', secondary=profile_department, back_populates='profiles')
    user = relationship("User", back_populates="profile")



class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    floor =  Column(Integer)

    profiles = relationship('Profile', secondary=profile_department, back_populates='departments')