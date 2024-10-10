# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# https://github.com/bosichong/sqlalchemy-test/blob/master/test_db.py
# sqlacodegen mysql+pymysql://root:rootroot@127.0.0.1:3306/msb_user_db --outfile models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建引擎
#create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")
engine = create_engine('mysql+pymysql://root:rootroot@127.0.0.1:3306/msb_user_db')

# 创建Session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'comment': '用户表'}

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, comment='用户昵称')
    phone = Column(String(255), nullable=False, comment='注册手机')
    PASSWORD = Column(String(255), comment='用户密码')


# 查询数据
query = session.query(User).filter(User.id > 1)
result = query.all()
for user in result:
    print(user)
