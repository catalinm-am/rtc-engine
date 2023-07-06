# Recipe To Cart

## 1. Data
- Stocam datele in Firestore (GCP) sa le putem accesa in FrontEnd/BackEnd
- Cum generam datele?
    - Inseram manual datele in Firestore
    - Sau Facem Data Scraping
- Avem urmatoarele entitati de stocat (`Customer`, `Product` si `Recipe`):
    ```python
    class Customer(BaseModel):
        customer_id: str
        price_range: Literal["premium", "fair", "cheap"]
    ```
    ```python
    class Product(BaseModel):
        id: str
        name: str
        image_url: str
        quantity: str
        description: str
        category: str # fructe & legume, carne, lactate, etc
        price: float
        reviews: Optional[int]
        rating: Optional[int]

    class ProductCart(Product):
        unit: int = 1
        recipe: List[str] = None
    ```
    ```python
    class Ingredient(BaseModel):
        name: str
        description: str
        quantity: str

    class Recipe(BaseModel):
        id: str
        name: str
        image_url: str
        category: str # vegetarian, desert, etc
        steps: List[str]
        ingredients: List[Ingredient]
        reviews: Optional[int]
        rating: Optional[int]
    ```

## 2. Endpoint (BackEnd)
- Cream un endpoint cu FastAPI in python
- Avem umatorul contract:
    ```python
    class Input(BaseModel):
        customer: Customer
        recipes: List[Union[Recipe, str]]

    class Output(BaseModel):
        products: List[ProductCart]
    ```
    - `/recipes_to_products`
    - Output
        - Returnam lista de produse necesare pentru o lista de retete
        - Ca logica, trebuie sa discutam aici cum facem mapare de la un ingredient, la un produs (folosim embeddings - pachetele sentence_transformers sau huggingface)
        - luam in considerare gramajul pentru toate retetele, etc (sunt mai multe variabile de luat in considerare, price_range de la customer, price de la product, etc)
    - Input
        - O reteta poate fi direct entitatea noastra de `Recipe` sau un `URL`
        - daca primim un URL extragem textul folosind un pachet de python
        - extragem din acest text, folosint ChatGPT de la Google, lista de ingrediente

## 3. FrontEnd (Vuetify3)
- Recipes Page
- Products Page
- Shopping Cart Page
- Visual Identity

## 4. Prezentarea
