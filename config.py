import os
from dotenv import load_dotenv

load_dotenv() 


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/yourdatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')
