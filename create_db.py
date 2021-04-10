from datetime import datetime
from flask import *
from flask_sqlalchemy import SQLAlchemy 
from app import db

if __name__ == '__main__':
   db.create_all()
