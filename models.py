import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, backref

from database import Base


JobDepartment = Table(
    'jobs_departments',
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('job_id', Integer, ForeignKey('jobs.id')),
    Column('department_id', Integer, ForeignKey('departments.id'))
)


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    departments = relationship(
        'Department',
        secondary=JobDepartment,
        back_populates='jobs'
    )


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    jobs = relationship(
        'Job',
        secondary=JobDepartment,
        back_populates='departments'
    )


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # is_superuser = Column(Boolean, default=False)

    profile = relationship('Profile', back_populates='user')
    tickets = relationship('Ticket', back_populates='owner')

    def deactivate_user(self):
        self.is_active = False


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    surmane = Column(String(30))
    patronymic = Column(String(20), nullable=True)
    user_id = Column(ForeignKey('users.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))
    department_id = Column(Integer, ForeignKey('jobs.id'))

    user = relationship('User', back_populates='profile')


SuperuserTicket = Table(
    'superuser_tickets',
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('superuser_id', Integer, ForeignKey('superusers.id')),
    Column('ticket_id', Integer, ForeignKey('tickets.id'))
)


class Superuser(Base):
    __tablename__ = 'superusers'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey('users.id'))


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    text = Column(String(1000))
    image = Column(String(1000), nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True, default=None)

    owner = relationship("User", back_populates="tickets")
    superusers = relationship(
        'Superuser',
        secondary=SuperuserTicket,
        backref='tickets'
    )
    comments = relationship('Comment', back_populates='ticket')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1000))
    image = Column(String(1000), nullable=True)
    user_id = Column(ForeignKey('users.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    parent_id = Column(Integer, ForeignKey('comments.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship('User', backref='comments')
    ticket = relationship('Ticket', back_populates='comments')
    replies = relationship(
        'Comment',
        backref=backref('parent', remote_side=[id]),
        lazy='dynamic'
    )
