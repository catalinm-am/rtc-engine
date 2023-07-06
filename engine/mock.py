import json 


#read a json file and load it into a python dictionary


def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data


# all_my_recipes = read_json_file('data/recipes.json')

## get 2 random recipes from the full list of recipes
def get_random_recipes(n=2):
    import random
    all_my_recipes = read_json_file('data/recipes.json')
    return random.sample(all_my_recipes, n)
