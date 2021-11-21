from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from static_variables import MAX_URL_LENGTH, MAX_METHOD_LENGTH

Base = declarative_base()


class Task1(Base):
    __tablename__ = 'unique_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)


class Task2(Base):
    __tablename__ = 'requests_stats'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(MAX_METHOD_LENGTH), nullable=False)
    count = Column(Integer, nullable=False)


class Task3(Base):
    __tablename__ = 'top_10_most_frequent'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(MAX_URL_LENGTH), nullable=False)
    count = Column(Integer, nullable=False)


class Task4(Base):
    __tablename__ = 'top_5_request_by_body_bytes_sent_with_4xx_status_code'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    status_code = Column(Integer, nullable=False)
    sent_size = Column(Integer, nullable=False)
    url = Column(String(MAX_URL_LENGTH), nullable=False)


class Task5(Base):
    __tablename__ = 'top_5_users_by_requests_count_with_5xx_status_code'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    count = Column(Integer, nullable=False)
