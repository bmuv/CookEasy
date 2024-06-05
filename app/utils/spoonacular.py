import os
import requests


API_KEY = os.environ.get('SPOONACULAR_API_KEY')


def fetch_recipes(ingredients):
    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={",".join(ingredients)}&apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()
