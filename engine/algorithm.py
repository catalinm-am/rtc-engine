import spacy
from typing import List, Optional
from pydantic import BaseModel
from engine.models.model import Recipe, Product, Ingredient
from engine.mock import all_available_products




def aggregate_ingredients(recipes: List[Recipe], products: List[Product] = all_available_products, similarity_threshold: float = 0.3) -> dict[str, Product]:
    nlp = spacy.load("ro_core_news_md")
    aggregated_ingredients = {}
    
    for recipe in recipes:
        for recipe_ingredient in recipe.ingredients:
            recipe_ingredient_tokens = nlp(recipe_ingredient.name)
            existing_ingredient = aggregated_ingredients.get(recipe_ingredient.name)
            
            if existing_ingredient:
                # Update existing ingredient with aggregated quantity
                existing_ingredient.quantity += recipe_ingredient.quantity
            else:
                # Add new ingredient to aggregated list
                aggregated_ingredients[recipe_ingredient.name] = recipe_ingredient
    
    matching_products = {}
    
    for ingredient_name, ingredient in aggregated_ingredients.items():
        ingredient_tokens = nlp(ingredient_name)
        recipe_ingredient_matches = []
        
        for product in products:
            product_tokens = nlp(product.name)
            similarity = ingredient_tokens.similarity(product_tokens)
            
            if similarity >= similarity_threshold:
                recipe_ingredient_matches.append((product, similarity)) #, abs(product.quantity - ingredient.quantity)
        
        if recipe_ingredient_matches:
            recipe_ingredient_matches = sorted(recipe_ingredient_matches, key=lambda x: x[1], reverse=True)  #lambda x: (x[1], x[2])
            
            matching_products[ingredient_name] = recipe_ingredient_matches[0][0]
    
    #transaform the matching products dictionary into a list
    matching_products = list(matching_products.values())

    return matching_products


# # Example usage
# recipes = [
#     Recipe(
#         id="1",
#         name="Chocolate Cake",
#         image_url="cake.jpg",
#         category="dessert",
#         steps=["Step 1", "Step 2", "Step 3"],
#         ingredients=[
#             Ingredient(name="făină", description="Făină albă", quantity=300, measurement_unit= "g"),
#             Ingredient(name="zahăr", description="Zahăr granulat", quantity=200, measurement_unit= 'g'),
#             Ingredient(name="cacao", description="Cacao neîndulcită", quantity=100, measurement_unit= 'g'),
#         ],
#         reviews=10,
#         rating=4
#     ),
#     Recipe(
#         id="2",
#         name="Vegetable Stir-Fry",
#         image_url="stir_fry.jpg",
#         category="vegetarian",
#         steps=["Step 1", "Step 2", "Step 3"],
#         ingredients=[
#             Ingredient(name="broccoli", description="Broccoli proaspăt", quantity=2, measurement_unit= 'buc'),
#             Ingredient(name="morcovi", description="Morcovi feliați", quantity=2, measurement_unit= 'buc'),
#             Ingredient(name="tofu", description="Tofu tare, cuburi", quantity=50, measurement_unit= 'g'),
#         ],
#         reviews=5,
#         rating=3
#     )
# ]

# products = [
#     Product(
#         id="1",
#         name="făină albă",
#         image_url="flour.jpg",
#         quantity="1000",
#         measurement_unit="g",
#         description="Făină versatilă pentru copt și gătit",
#         category="păntry",
#         price=2.99,
#         reviews=100,
#         rating=4
#     ),
#     Product(
#         id="2",
#         name="zahăr granulat",
#         image_url="sugar.jpg",
#         quantity="500",
#         measurement_unit="g",
#         description="Îndulcitor comun pentru băuturi și deserturi",
#         category="păntry",
#         price=5.5,
#         reviews=100,
#         rating=4
#     ), 
#     Product(
#         id="3",
#         name="cacao neîndulcită",
#         image_url="cocoa.jpg",
#         quantity="200",
#         measurement_unit="g",
#         description="Cacao naturală pentru prăjituri și băuturi calde",
#         category="păntry",
#         price=3.49,
#         reviews=80,
#         rating=4
#     ),
#     Product(
#         id="4",
#         name="ulei de măsline extra virgin",
#         image_url="olive_oil.jpg",
#         quantity="500",
#         measurement_unit="ml",
#         description="Ulei de măsline presat la rece, de calitate superioară",
#         category="păntry",
#         price=7.99,
#         reviews=120,
#         rating=5
#     ),
#     Product(
#         id="5",
#         name="ciocolată neagră 70%",
#         image_url="dark_chocolate.jpg",
#         quantity="100",
#         measurement_unit="g",
#         description="Ciocolată neagră cu conținut ridicat de cacao",
#         category="dulciuri",
#         price=2.49,
#         reviews=90,
#         rating=4
#     ),
#     Product(
#         id="6",
#         name="ardei gras roșu",
#         image_url="red_pepper.jpg",
#         quantity="1",
#         measurement_unit="buc",
#         description="Ardei gras roșu, proaspăt și aromat",
#         category="fructe & legume",
#         price=1.29,
#         reviews=50,
#         rating=4
#     ),
#     Product(
#         id="7",
#         name="zahăr pudra",
#         image_url="sugar.jpg",
#         quantity="300",
#         measurement_unit="g",
#         description="Îndulcitor comun pentru băuturi și deserturi",
#         category="păntry",
#         price=5.5,
#         reviews=100,
#         rating=4
#     ),
# ]



# test = aggregate_ingredients(recipes,products)


# print(test)