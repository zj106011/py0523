# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Car(Base):
    __tablename__ = 'cars'

    cid = Column(Integer, primary_key=True)
    pid = Column(ForeignKey('purchasers.pid', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    brand = Column(String(32), nullable=False)
    ctype = Column(String(32), nullable=False)
    price = Column(Float)
    purchased_at = Column(DateTime)

    purchaser = relationship('Purchaser', primaryjoin='Car.pid == Purchaser.pid', backref='cars')


class Purchaser(Base):
    __tablename__ = 'purchasers'

    pid = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    idcard = Column(String(18), nullable=False)
    sex = Column(ENUM('男', '女'))
