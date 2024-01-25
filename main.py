from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer,String,DateTime,Column
from datetime import datetime
from sqlalchemy import create_engine
engine=create_engine(url='sqlite:///sample.db',echo=True)

Base=declarative_base()

"""
User class
id  integer
username string
email string
date_created datetime
"""


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(20),unique=True,nullable=False)
    email=Column(String(30),nullable=True,unique=True)
    date_created=Column(DateTime(),default=datetime.utcnow)


    def __repr__(self):
        return f'username is {self.username} and email is {self.email} '
    

u1=User(username='shreya',email='vaish@gmail.com')
print(u1)


Base.metadata.create_all(engine)