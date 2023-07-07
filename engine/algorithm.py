import spacy
from typing import List, Optional
from pydantic import BaseModel
from engine.models.model import Recipe, Product, Ingredient, MultiplierProduct
from engine.mock import all_available_products
from math import ceil
from fractions import Fraction
import re




# def aggregate_ingredients(recipes: List[Recipe], products: List[Product] = all_available_products, similarity_threshold: float = 0.3) -> dict[str, Product]:
#     nlp = spacy.load("ro_core_news_md")
#     aggregated_ingredients = {}
    
#     for recipe in recipes:
#         for recipe_ingredient in recipe.ingredients:
#             recipe_ingredient_tokens = nlp(recipe_ingredient.name)
#             existing_ingredient = aggregated_ingredients.get(recipe_ingredient.name)
            
#             if existing_ingredient:
#                 # Update existing ingredient with aggregated quantity
#                 existing_ingredient.quantity += recipe_ingredient.quantity
#             else:
#                 # Add new ingredient to aggregated list
#                 aggregated_ingredients[recipe_ingredient.name] = recipe_ingredient
    
#     matching_products = {}
    
#     for ingredient_name, ingredient in aggregated_ingredients.items():
#         ingredient_tokens = nlp(ingredient_name)
#         recipe_ingredient_matches = []
        
#         for product in products:
#             product_tokens = nlp(product.name)
#             similarity = ingredient_tokens.similarity(product_tokens)
            
#             if similarity >= similarity_threshold:
#                 recipe_ingredient_matches.append((product, similarity)) #, abs(product.quantity - ingredient.quantity)
        
#         if recipe_ingredient_matches:
#             recipe_ingredient_matches = sorted(recipe_ingredient_matches, key=lambda x: x[1], reverse=True)  #lambda x: (x[1], x[2])
            
#             matching_products[ingredient_name] = recipe_ingredient_matches[0][0]
    
#     #transaform the matching products dictionary into a list
#     matching_products = list(matching_products.values())

#     return matching_products


def remove_non_numbers(string):
    # Remove anything that is not a number, fraction, or decimal float number
    cleaned_string = re.sub(r'[^0-9./]', '', string)
    return cleaned_string


def convert_fraction_str_to_float(a:str):
    try:
        return float(a)
    except:
        try:
            return float(Fraction(a)) 
        except:
            a = remove_non_numbers(a)
            return float(Fraction(a)) 



def aggregate_ingredients(recipes: List[Recipe], products: List[Product]= all_available_products, similarity_threshold: float = 0.3) -> dict[str, Product]:
    nlp = spacy.load("ro_core_news_md")
    aggregated_ingredients = {}
    aggregated_ingredient_names = set()

    for recipe in recipes:
        for recipe_ingredient in recipe.ingredients:
            recipe_ingredient_tokens = nlp(recipe_ingredient.name)
            existing_ingredient = aggregated_ingredients.get(recipe_ingredient.name)

            if existing_ingredient:
                # Update existing ingredient with aggregated quantity
                existing_ingredient.quantity = convert_fraction_str_to_float(existing_ingredient.quantity)
                recipe_ingredient.quantity = convert_fraction_str_to_float(recipe_ingredient.quantity)
                existing_ingredient.quantity += recipe_ingredient.quantity
            else:
                # Add new ingredient to aggregated list
                recipe_ingredient.quantity = convert_fraction_str_to_float(recipe_ingredient.quantity)
                aggregated_ingredients[recipe_ingredient.name] = recipe_ingredient

    matching_products = {}

    for ingredient_name, ingredient in aggregated_ingredients.items():
        ingredient_tokens = nlp(ingredient_name)
        recipe_ingredient_matches = []

        for product in products:
            product.quantity = convert_fraction_str_to_float(product.quantity)
            product_tokens = nlp(product.name)
            similarity = ingredient_tokens.similarity(product_tokens)

            if similarity >= similarity_threshold:
                recipe_ingredient_matches.append((product, similarity))

        if recipe_ingredient_matches:
            recipe_ingredient_matches = sorted(recipe_ingredient_matches, key=lambda x: x[1], reverse=True)
            best_match_product = recipe_ingredient_matches[0][0]
            best_match_product.quantity = convert_fraction_str_to_float(best_match_product.quantity)
            default_multiplier = 1  # Default multiplier

            if isinstance(best_match_product, MultiplierProduct):
                best_match_product.multiplier = default_multiplier
                best_match_product.quantity = convert_fraction_str_to_float(best_match_product.quantity)
            else:
                # print(best_match_product)
                # print(type(best_match_product))
                best_match_product.multiplier = default_multiplier
                best_match_product.quantity = convert_fraction_str_to_float(best_match_product.quantity)

                best_match_product = MultiplierProduct(**best_match_product.dict())
            
            best_match_product.quantity = convert_fraction_str_to_float(best_match_product.quantity)
            if best_match_product.quantity < ingredient.quantity:
                default_multiplier = ceil(ceil(ingredient.quantity) / ceil(best_match_product.quantity))  # Calculate multiplier

            best_match_product.multiplier = default_multiplier  # Assign multiplier to the best match product
            matching_products[ingredient_name] = best_match_product

    return matching_products