from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

import json
import openai

# openai.organization = "adore me"
openai.api_key = ""
# openai.Model.list()


from starlette.responses import (
    JSONResponse,
    RedirectResponse,
)

from engine.models.model import (Ingredient, Recipe, Product, InputRecipeURL, InputRecipes)
from engine.mock import (get_random_recipes, get_duplicate_recipe)
from engine.algorithm import (aggregate_ingredients, aggregate_ingredients1, aggregate_ingredients2)


images = {
    "https://www.lauralaurentiu.ro/retete-culinare/deserturi-dulciuri-de-casa/coliva-reteta-traditionala-din-grau-cu-multa-nuca.html": "https://www.lauralaurentiu.ro/wp-content/uploads/2019/03/coliva-reteta-traditionala-cu-nuca-si-grau.jpg",
    "https://savoriurbane.com/papanasi-prajiti-reteta-traditionala-cu-smantana-si-dulceata/": "https://savoriurbane.com/wp-content/uploads/2018/01/papanasi-inecati-in-smantana-si-dulceata-reteta.jpg",
    "https://pofta-buna.com/salata-boeuf-piept-pui-varianta-romaneasca/": "https://pofta-buna.com/wp-content/uploads/2019/10/salata-boeuf-cu-piept-de-pui-1-500x375.jpg",
    "https://www.lauralaurentiu.ro/retete-culinare/deserturi-dulciuri-de-casa/moelleux-au-chocolat.html": "https://www.lauralaurentiu.ro/wp-content/uploads/2014/07/moelleux-au-chocolat-1.jpg",
}


## initialize the app
app = FastAPI( title="Foodie API", description="This is the API for the Foodie app", version="0.1.0")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8090",
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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





@app.post("/recipe_to_products")
async def recipe_to_products(request: InputRecipes):
    """
    This endpoint will convert a list of recipes to a list of products
    """

    # mock_recipe = get_random_recipes(2)
    # mock_recipe = get_duplicate_recipe()
    # print(mock_recipe)

    product_list = aggregate_ingredients2(request.recipes)
    product_list = [p.dict() for p in product_list]
    for p in product_list:
        p["unit"] = p["multiplier"]
    return product_list


# @lru_cache(maxsize=32)
def get_recipe(url):
    messages = [{
        "role": "user",
        "content": f"""
            Ai urmatorul link: {url}
            Te rog scrie-mi un fisier json care sa respecte urmatoarea structura:
            
            class Recipe(BaseModel):
                id: str
                name: str
                description: str
                image_url: str
                category: str
                servings: int
                steps: List[str]
                ingredients: List[Ingredient]
                reviews: Optional[int]
                rating: Optional[float]

            Ingredient e de forma:
            class Ingredient(BaseModel):
                name: str
                quantity: str
                measure_unit: str
        """
    }]

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    
    return chat.choices[0].message.content


@app.post('/recipe', response_model=Recipe)
async def url_recipe(request: InputRecipeURL):
    try:
        recipe =  Recipe.parse_obj(json.loads(get_recipe(request.url)))
        recipe.image_url = images.get(request.url, "")
        return recipe
    except Exception:
        raise HTTPException(status_code=400, detail="Cound not generate recipe.")
