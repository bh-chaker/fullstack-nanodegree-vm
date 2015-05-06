from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
  """Database table 'user'. Contains information about a User"""
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)
  picture = Column(String(250))


class Category(Base):
  """Database table 'category'. Contains information about a Category"""
  __tablename__ = 'category'
  __table_args__ = (UniqueConstraint('name', name='uix_1'),)

  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
  description = Column(String(1024))
  image_url = Column(String(2048))
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship(User)

  @property
  def serialize(self):
    """Return object data in easily serializeable format"""
    return {
      'name'         : self.name,
      'description'  : self.description,
      'id'           : self.id,
      'image_url'    : self.image_url,
    }

class Item(Base):
  """Database table 'item'. Contains information about a Item"""
  __tablename__ = 'item'
  __table_args__ = (UniqueConstraint('category_id', 'name', name='uix_2'),)

  id = Column(Integer, primary_key = True)
  name = Column(String(80), nullable = False)
  description = Column(String(1024))
  image_url = Column(String(2048))
  category_id = Column(Integer,ForeignKey('category.id'))
  category = relationship(Category)
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship(User)

  @property
  def serialize(self):
    """Return object data in easily serializeable format"""
    return {
      'name'         : self.name,
      'description'  : self.description,
      'image_url'    : self.image_url,
      'id'           : self.id,
    }

#Connect to SQL lite database file and create the database tables
engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
