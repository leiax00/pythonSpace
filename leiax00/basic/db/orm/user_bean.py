# coding: utf-8
from os.path import dirname

from sqlalchemy import Column, String, Integer, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    login = Column(String(225))
    id = Column(Integer, primary_key=True)
    name = Column(String(225))


if __name__ == '__main__':
    db_name = 'demo'
    driver = 'mysql://root@localhost/{0}'.format(db_name)
    try:
        eng = create_engine(driver)
    except ImportError:
        raise RuntimeError()
    try:
        eng.connect()
    except exc.OperationalError:
        eng = create_engine(driver)
        eng.execute('CREATE DATABASE {0}'.format(dirname(db_name)))
        eng = create_engine(driver)
    Session = orm.sessionmaker(bind=eng)
    ses = Session()
    user = User.__table__
    eng = user.metadata.bind = eng
    # insert
    ses.add_all(User('a', 12, 'a'))
