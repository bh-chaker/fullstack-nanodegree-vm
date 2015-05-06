from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from database_setup import Base, Category, Item, User

#Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
database_session = DBSession()

#User Helper Functions
def createUser(user_info):
  """Add user to database and return the user id"""
  newUser = User(name = user_info['username'], email = user_info['email'],
    picture = user_info['picture'])
  database_session.add(newUser)
  database_session.commit()
  return getUserID(user_info['email'])

def getUser(user_id):
  """Get user from database by user id"""
  user = database_session.query(User).filter_by(id = user_id).one()
  return user

def getUserID(email):
  """Checks if email exists in database.
  Returns user id if user exists, else returns None"""
  try:
      user = database_session.query(User).filter_by(email = email).one()
      return user.id
  except:
      return None

def getCategories():
  """Gets all categories from database"""
  return database_session.query(Category).order_by(asc(Category.name))

def getCategory(category_name):
  """Gets category from database by category name"""
  return database_session.query(Category).filter_by(name = category_name).one()

def getItem(category_name, item_name):
  """Gets item from database by category name and item name"""
  category = getCategory(category_name)
  return database_session.query(Item).filter_by(category_id = category.id,
    name = item_name).one()

def getItems(category_name):
  """Gets all items of a category from database by category name"""
  category = getCategory(category_name)
  return database_session.query(Item).filter_by(
    category_id = category.id).order_by(asc(Item.id))

def addItem(data):
  """Adds item to database.
  Returns True if operation succeeded, else returns False"""
  database_session.add(Item(**data))
  try:
    database_session.commit()
    return True
  except IntegrityError:
    database_session.rollback()
    return False

def updateItem(item, data):
  """Updates item with new information.
  Returns True if operation succeeded, else returns False"""
  if data['name']:
    item.name = data['name']
  if data['description']:
    item.description = data['description']
  if data['image_url']:
    item.image_url = data['image_url']

  database_session.add(item)
  try:
    database_session.commit()
    return True
  except IntegrityError:
    database_session.rollback()
    return False

def removeItem(item):
  """Removes an item from the database."""
  database_session.delete(item)
  database_session.commit()
  return True