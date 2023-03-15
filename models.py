from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from .database import Base


JobDepartment = Table(
    'jobs_departments',
    Column('id', Integer, primary_key=True, index=True),
    Column('job_id', Integer, ForeignKey('Job.id')),
    Column('department_id', Integer, ForeignKey('Department.id'))
)

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    departments = relationship(
        'Department',
        secondary=JobDepartment,
        backref='Job'
    )


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    jobs = relationship(
        'Job',
        secondary=JobDepartment,
        backref='Department'
    )


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    profile = relationship('Profile', back_populates='user')
    tickets = relationship('Ticket', back_populates='user')


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    surmane = Column(String(30))
    patronymic = Column(String(20))
    user_id = Column(ForeignKey('User.id'))
    job_id = Column(Integer, ForeignKey('Job.id'))
    department_id = Column(Integer, ForeignKey('Job.id'))

    user = relationship('User', back_populates='profile')


SuperuserTicket = Table(
    'superuser_tickets',
    Column('id', Integer, primary_key=True, index=True),
    Column('superuser_id', Integer, ForeignKey('Superuser.id')),
    Column('ticket_id', Integer, ForeignKey('Ticket.id'))
)


class Superuser(Base):
    __tablename__ = 'superusers'
    user_id = Column(ForeignKey('User.id'))
    tickets = relationship(
        'Ticket',
        secondary=SuperuserTicket,
        backref='Superuser'
    )


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    text = Column(String(1000))
    image = Column(String(1000))
    owner_id = Column(Integer, ForeignKey('User.id'))
    
    owner = relationship("User", back_populates="tickets")
    superusers = relationship(
        'Superuser',
        secondary=SuperuserTicket,
        backref='tickets'
    )
    comments = relationship('Comment', backref='ticket')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1000))
    image = Column(String(1000))
    user_id = Column(ForeignKey('User.id'))
    ticket_id = Column(Integer, ForeignKey('Ticket.id'))
    parent_id = Column(Integer, ForeignKey('Comment.id'))

    user = relationship('User', backref='comments')
    ticket = relationship('Ticket', backref='comments')
    replies = relationship(
        'Comment',
        backref=backref('parent', remote_side=[id]),
        lazy='dynamic'
    )