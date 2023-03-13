from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

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
    departments = relationship('Department', secondary=JobDepartment, backref='Job')


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    jobs = relationship('Job', secondary=JobDepartment, backref='Department')


SuperuserTicket = Table(
    'superuser_tickets',
    Column('id', Integer, primary_key=True, index=True),
    Column('superuser_id', Integer, ForeignKey('Superuser.id')),
    Column('ticket_id', Integer, ForeignKey('Ticket.id'))
)


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Superuser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    tickets = relationship('Ticket', secondary=SuperuserTicket, backref='Superuser')


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    surmane = Column(String(30))
    patronymic = Column(String(20))
    job_id = Column(Integer, ForeignKey('Job.id'))
    department_id = Column(Integer, ForeignKey('Job.id'))


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(1000))
    owner = Column(ForeignKey('User.id'))
    
    owner = relationship("User", back_populates="tickets")
    superusers = relationship('Superuser', secondary=SuperuserTicket, backref='Ticket')
