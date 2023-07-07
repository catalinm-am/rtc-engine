from pydantic import BaseModel
from typing import List, Optional


class Ingredient(BaseModel):
    name: str
    quantity: str
    measure_unit: str


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


class Product(BaseModel):
    id: str
    name: str
    image_url: Optional[str]
    quantity: str
    measure_unit: str
    description: str
    category: str # fructe & legume, carne, lactate, etc
    price: float


class InputRecipeURL(BaseModel):
    url: str
