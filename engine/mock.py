import json 
from engine.models.model import Recipe, Product
import random

#read a json file and load it into a python dictionary


def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


# all_my_recipes = read_json_file('data/recipes.json')

## get 2 random recipes from the full list of recipes
def get_random_recipes(n=2):
    
    all_my_recipes = read_json_file('data/recipes.json')
    # transform the list of dictionaries into a list of Recipe objects
    all_my_recipes = [Recipe(**recipe_dict) for recipe_dict in all_my_recipes]
    #return a random sample of n recipes
    return random.sample(all_my_recipes, n)



# create a mock function that returns a list that duplicates one of the recipes in the original list
def get_duplicate_recipe():
    all_my_recipes = read_json_file('data/recipes.json')
    # transform the list of dictionaries into a list of Recipe objects
    all_my_recipes = [Recipe(**recipe_dict) for recipe_dict in all_my_recipes]
    #duplicate a random recipe in the list
    random_recipe = random.choice(all_my_recipes)
    return [random_recipe, random_recipe]

def get_all_available_products():

    all_products = read_json_file('data/products.json')
    #transaform the list of dictionaries into a list of Product objects
    # print(all_products)

    all_products = [Product(**product_dict) for product_dict in all_products]
    # print(all_products)
    return all_products


all_available_products = get_all_available_products()

# print(all_available_products)