from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name,votes):
    cat_object = Cat(
    	name=name,
    	votes=votes)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_cat(cat_id):
	cat = session.query(Cat).filter_by(id=cat_id).first()
	return cat

def vote_cat(cat_id):
	cat = session.query(Cat).filter_by(id=cat_id).first()
	cat.votes += 1
	session.commit()