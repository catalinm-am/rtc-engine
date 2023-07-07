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
    new_servings: Optional[int]  # New column for servings
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
    multiplier: Optional[int]  # New column for multiplier


class MultiplierProduct(Product):
    multiplier: int