from fastapi import FastAPI, Request, Response
import json

from starlette.responses import (
    JSONResponse,
    RedirectResponse,
)

from engine.models.model import (Ingredient, Recipe, Product)
from engine.mock import (get_random_recipes, get_duplicate_recipe)
from engine.algorithm import (aggregate_ingredients)


## initialize the app
app = FastAPI( title="Foodie API", description="This is the API for the Foodie app", version="0.1.0")

@app.middleware("http")
async def setup_request(request: Request, call_next) -> JSONResponse:
    """ A middleware for setting up a request. It creates a new request_id
        and adds some basic metrics.

        Args:
            request: The incoming request
            call_next (obj): The wrapper as per FastAPI docs

        Returns:
            response: The JSON response
    """
    response = await call_next(request)

    return response





@app.get("/recipe_to_products/{request}")
async def recipe_to_products(request: str):
    """
    This endpoint will convert a list of recipes to a list of products
    """

    # mock_recipe = get_random_recipes(2)
    mock_recipe = get_duplicate_recipe()

    # print(mock_recipe)

    product_list = aggregate_ingredients(mock_recipe)



    # data = { "id": "1", "name": "mere", "image_url": "www.example.com",  "quantity": "2", "measure_unit": "g", "description":"", "category":"3", "price": "1.0", "reviews": "2", "rating": "3"}

    # product = [Product(**data)]

    return product_list



