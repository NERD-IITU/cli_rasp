from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Block(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Bundle(Base):
    __tablename__ = 'bundles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Week(Base):
    __tablename__ = 'week'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Time(Base):
    __tablename__ = 'times'
    id = Column(Integer, primary_key=True)
    start_time = Column(String(250), nullable=False)
    end_time = Column(String(250), nullable=False)

    def __init__(self, id, start_time, end_time):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time




class Timetable(Base):

    __tablename__='timetable'
    id = Column(Integer, primary_key=True)
    weekid = Column(Integer, ForeignKey('week.id'))
    week = relationship(Week)
    blockid = Column(Integer, ForeignKey('blocks.id'))
    blocks = relationship(Block)
    bundleid = Column(Integer, ForeignKey('bundles.id'))
    bundles = relationship(Bundle)
    teacherid = Column(Integer, ForeignKey('teachers.id'))
    teachers = relationship(Teacher)
    timeid = Column(Integer, ForeignKey('times.id'))
    times = relationship(Time)
    subjectid = Column(Integer, ForeignKey('subjects.id'))
    subjects = relationship(Subject)


    def __init__(self,id,weekid,blockid,bundleid,teacherid,timeid,subjectid):
        self.id = id
        self.weekid = weekid
        self.blockid = blockid
        self.bundleid = bundleid
        self.teacherid = teacherid
        self.timeid = timeid
        self.subjectid = subjectid



engine = create_engine('sqlite:///schedule.db')

Base.metadata.create_all(engine)
