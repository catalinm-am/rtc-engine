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


def get_mock_product_list(recipe_name:str):
    existing_products_list = {
        "Ciorba Radauteana" : [ 
            {
            "id": "156",
            "name": "Piept de pui dezosat 500g",
            "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/9c/d9/5b01149bb51d6b2d42edc3f7ce16.jpg",
            "quantity": 500,
            "measure_unit": "g",
            "description": "Puiul Gospodarului",
            "category": "Carne si Peste",
            "price": 19.99,
            "multiplier": 1,
            "unit": 1
            },
                {
        "id": "794",
        "name": "Smântână 12% grăsime 190g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/cf/13/60193eefa89d2f5a78bfc8fdec70.jpg",
        "quantity": "190.0",
        "measure_unit": "g",
        "description": "HUZUR",
        "category": "Lactate, Branzeturi si Oua",
        "price": 2.99,
        "reviews": null,
        "rating": null
    },

        {
        "id": "1253",
        "name": "Ouă proaspete de la găini crescute la sol, mărimea M, 10 buc",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/71/9c/0959d595805f2aa499b10a6a745b.jpg",
        "quantity": "1.0",
        "measure_unit": "buc",
        "description": "Din Ogradă",
        "category": "Lactate, Branzeturi si Oua",
        "price": 11.99,
        "reviews": null,
        "rating": null
    },
    {
        "id": "4121",
        "name": "Oțet din alcool etilic rafinat 1l",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/46/63/29ca23708358cc7d8e87aa131237.jpg",
        "quantity": "1.0",
        "measure_unit": "l",
        "description": "Olympia",
        "category": "Ulei si Otet",
        "price": 2.99,
        "reviews": null,
        "rating": null
    },
    {
        "id": "367",
        "name": "Păstârnac rădăcină România 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/6f/8e/b3facd0c25d49519aed0434fc6d0.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 8.49,
        "reviews": null,
        "rating": null
    },
    {
        "id": "429",
        "name": "Ceapă galbenă 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/38/23/b343064662582b3894ef8944b3c2.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 6.99,
        "reviews": null,
        "rating": null
    },
    {
        "id": "3453",
        "name": "Ardei gras copt în oțet 680g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/2d/7b/45039d4d719a77093412fccb0a7c.jpg",
        "quantity": "680.0",
        "measure_unit": "g",
        "description": "Vasluianca",
        "category": "Conserve",
        "price": 11.99,
        "reviews": null,
        "rating": null
    },
    {
        "id": "421",
        "name": "Morcovi eco 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/83/96/c77d0e04e790abc415b234b4ca74.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 5.97,
        "reviews": null,
        "rating": null
    },
        {
        "id": "427",
        "name": "Țelină rădăcină 1 buc",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/1a/7b/351d8bd3f450bc72ae4cb39d6878.jpg",
        "quantity": "1.0",
        "measure_unit": "buc",
        "description": "",
        "category": "Fructe si Legume",
        "price": 7.69,
        "reviews": null,
        "rating": null
    },
    {
        "id": "459",
        "name": "Usturoi eco 150g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/f1/8e/14c0843d77582a94921570e5cf29.jpg",
        "quantity": "150.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 5.69,
        "reviews": null,
        "rating": null
    },

    {
        "id": "3635",
        "name": "Foi dafin 4g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/da/ae/c9424b95e606326c36e23abaab0b.jpg",
        "quantity": "4.0",
        "measure_unit": "g",
        "description": "Cosmin",
        "category": "Condimente si Sosuri",
        "price": 1.69,
        "reviews": null,
        "rating": null
    },
        {
        "id": "3659",
        "name": "Sare de mare iodată 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/cc/06/a17e68118fda2f195ab9cd66a3e7.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "Kalas",
        "category": "Condimente si Sosuri",
        "price": 11.5,
        "reviews": null,
        "rating": null
    },    
    {
        "id": "3760",
        "name": "Piper negru măcinat 36g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/56/7f/ceff5e9dc00e8d4165e072c3e631.jpg",
        "quantity": "36.0",
        "measure_unit": "g",
        "description": "Kamis",
        "category": "Condimente si Sosuri",
        "price": 9.39,
        "reviews": null,
        "rating": null
    } ],


    "Indian Chicken Curry" : [
            {
            "id": "156",
            "name": "Piept de pui dezosat 500g",
            "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/9c/d9/5b01149bb51d6b2d42edc3f7ce16.jpg",
            "quantity": 500,
            "measure_unit": "g",
            "description": "Puiul Gospodarului",
            "category": "Carne si Peste",
            "price": 19.99,
            "multiplier": 1,
            "unit": 1
            },
    {
        "id": "4120",
        "name": "Ulei rafinat de floarea-soarelui 1l",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/c5/ea/83b0f6791080f43570a031340743.jpg",
        "quantity": "1.0",
        "measure_unit": "l",
        "description": "Delicia",
        "category": "Ulei si Otet",
        "price": 4.99,
        "reviews": null,
        "rating": null
    },
    {
        "id": "424",
        "name": "Ceapa galbena 1kg",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/2b/fb/4cdc2d2a09b2167a89f1fdb0c08d.jpg",
        "quantity": "1.0",
        "measure_unit": "kg",
        "description": "",
        "category": "Fructe si Legume",
        "price": 9.49,
        "reviews": null,
        "rating": null
    },
    {
        "id": "459",
        "name": "Usturoi eco 150g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/f1/8e/14c0843d77582a94921570e5cf29.jpg",
        "quantity": "150.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 5.69,
        "reviews": null,
        "rating": null
    },

        {
        "id": "3688",
        "name": "Ghimbir 15g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/6d/07/bf80750b50fd175e2ac841efd360.jpg",
        "quantity": "15.0",
        "measure_unit": "g",
        "description": "Kamis",
        "category": "Condimente si Sosuri",
        "price": 3.85,
        "reviews": null,
        "rating": null
    },
    {
        "id": "3784",
        "name": "Curry 25g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/9e/cc/8e4a2dea40f97f0a89ccc0752874.jpg",
        "quantity": "25.0",
        "measure_unit": "g",
        "description": "Kamis",
        "category": "Condimente si Sosuri",
        "price": 3.85,
        "reviews": null,
        "rating": null
    },
    {
        "id": "471",
        "name": "Turmeric 50g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/7f/7e/3db378e0776f0df27b83214d8989.jpg",
        "quantity": "50.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 6.39,
        "reviews": null,
        "rating": null
    },
    {
        "id": "3668",
        "name": "Boia de ardei iute 17g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/a6/a7/a0162ee5140e20a96281a558a032.jpg",
        "quantity": "17.0",
        "measure_unit": "g",
        "description": "Cosmin",
        "category": "Condimente si Sosuri",
        "price": 1.69,
        "reviews": null,
        "rating": null
    },

        {
        "id": "3760",
        "name": "Piper negru macinat 36g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/56/7f/ceff5e9dc00e8d4165e072c3e631.jpg",
        "quantity": "36.0",
        "measure_unit": "g",
        "description": "Kamis",
        "category": "Condimente si Sosuri",
        "price": 9.39,
        "reviews": null,
        "rating": null
    },


    {
        "id": "362",
        "name": "Rosii Romania 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/64/20/f3f12f1937e6c98df7f9bf965425.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "",
        "category": "Fructe si Legume",
        "price": 5.89,
        "reviews": null,
        "rating": null
    },

        {
        "id": "3646",
        "name": "Sos de rosii Arrabbiata 400g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/ac/14/282e9a33e5f400bffd5e32546cd6.jpg",
        "quantity": "400.0",
        "measure_unit": "g",
        "description": "Barilla",
        "category": "Condimente si Sosuri",
        "price": 10.9,
        "reviews": null,
        "rating": null
    },

     {
        "id": "948",
        "name": "Iaurt natural 5% grasime 300g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/ca/16/481a7d8fb849728f4698d922eef1.jpg",
        "quantity": "300.0",
        "measure_unit": "g",
        "description": "Laptaria cu caimac",
        "category": "Lactate, Branzeturi si Oua",
        "price": 6.89,
        "reviews": null,
        "rating": null
    },
    {
        "id": "508",
        "name": "Conopida murata 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/0f/4b/3323124bb9412574afee13563ccf.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "Biolider",
        "category": "Fructe si Legume",
        "price": 6.99,
        "reviews": null,
        "rating": null
    },
    {
        "id": "2861",
        "name": "Orez cu bob rotund 1kg",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/7a/43/f0a0994bef6f5e83775b73b9cc11.jpg",
        "quantity": "1.0",
        "measure_unit": "kg",
        "description": "Atifco",
        "category": "Paste si Orez",
        "price": 6.49,
        "reviews": null,
        "rating": null
    }],

    "Cheesecake cu fructe de padure": [
            {
        "id":"fursecuri_cu_ciocolata",
        "name":"Fursecuri cu ciocolata",
        "image_url": "https://jamilacuisine.ro/wp-content/uploads/2016/04/Fursecuri-cu-ciocolata-si-unt-de-arahide-500x478.jpg",
        "quantity":"250",
        "measure_unit":"g",
        "description":"Fursecuri faramitate cu ciocolata",
        "category":"dulciuri",
        "price":15.99,
        "reviews":null,
        "rating":null
    },
        {
        "id":"fructe_de_padure_congelate",
        "name":"Fructe de padure congelate",
        "image_url":"https://storage.googleapis.com/bringoimg/web/cache/sylius_shop_product_original/a1/b4/1b16357ba2ba9cfa766cf95d417a.jpg",
        "quantity":"350 g",
        "measure_unit":"g",
        "description":"Mix de fructe de padure congelate",
        "category":"fructe & legume",
        "price":10.99,
        "reviews":null,
        "rating":null
    },
        {
        "id": "897",
        "name": "Unt 60% grasime, 180g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/97/18/95cf14dc84f1843ac775d4930401.jpg",
        "quantity": "180.0",
        "measure_unit": "g",
        "description": "Bunisim",
        "category": "Lactate, Branzeturi si Oua",
        "price": 8.89,
        "reviews": null,
        "rating": null
    },
        {
        "id": "4140",
        "name": "Suc de lamaie 200ml",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/b7/51/43dc7e3b9edde0cc0832e7a0aebb.jpg",
        "quantity": "200.0",
        "measure_unit": "ml",
        "description": "Limmi",
        "category": "Ulei si Otet",
        "price": 5.89,
        "reviews": null,
        "rating": null
    },
 {
        "id": "4299",
        "name": "Foi de gelatina 10g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/55/f4/e7792bb972e3155f5d232547ce1c.jpg",
        "quantity": "10.0",
        "measure_unit": "g",
        "description": "Dr. Oetker",
        "category": "Faina si Zahar",
        "price": 5.41,
        "reviews": null,
        "rating": null
    },
    {
        "id":"lapte_condensat_indulcit",
        "name":"Lapte condensat indulcit",
        "image_url":"https://example.com//lapte-condensat.jpg",
        "quantity":"1",
        "measure_unit":"buc",
        "description":"Cutie de lapte condensat indulcit",
        "category":"lactate",
        "price":7.99,
        "reviews":null,
        "rating":null
    },
    {
        "id": "824",
        "name": "Branza de vaci 6% grasime, 200g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/4e/9a/059b63040f847e412df6c398d8e1.jpg",
        "quantity": "200.0",
        "measure_unit": "g",
        "description": "Covalact",
        "category": "Lactate, Branzeturi si Oua",
        "price": 7.55,
        "reviews": null,
        "rating": null
    },

        {
        "id": "1364",
        "name": "Mascarpone 250g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/47/16/683951f57471cc9443ff40e569a5.jpg",
        "quantity": "250.0",
        "measure_unit": "g",
        "description": "FORMAGIA",
        "category": "Lactate, Branzeturi si Oua",
        "price": 12.99,
        "reviews": null,
        "rating": null
    }
    ],

    "Paste Carbonara": [
    {
        "id": "1508",
        "name": "Pecorino Romano DOP 250g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/a7/46/92edb80d2ac055da92fbd7869bbe.jpg",
        "quantity": "250.0",
        "measure_unit": "g",
        "description": "Zanetti",
        "category": "Lactate, Branzeturi si Oua",
        "price": 35.99,
        "reviews": null,
        "rating": null
    },

    {
        "id":"guanciale",
        "name":"Guanciale",
        "image_url": "https://www.mashed.com/img/gallery/what-is-guanciale-and-why-is-it-so-expensive/l-intro-1622579130.jpg",
        "quantity":"300",
        "measure_unit":"g",
        "description":"",
        "category":"carne",
        "price":27.0,
        "reviews":null,
        "rating":null
    },

        {
        "id": "2890",
        "name": "Paste Spaghetti n.15, 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/35/29/2388ffac17bb8ca5f16693681138.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "La Molisana",
        "category": "Paste si Orez",
        "price": 7.69,
        "reviews": null,
        "rating": null
    },

            {
        "id": "1253",
        "name": "Ouă proaspete de la găini crescute la sol, mărimea M, 10 buc",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/71/9c/0959d595805f2aa499b10a6a745b.jpg",
        "quantity": "1.0",
        "measure_unit": "buc",
        "description": "Din Ogradă",
        "category": "Lactate, Branzeturi si Oua",
        "price": 11.99,
        "reviews": null,
        "rating": null
    },
        {
        "id": "3659",
        "name": "Sare de mare iodată 500g",
        "image_url": "https://cdn.freshful.ro/media/cache/sylius_shop_product_thumbnail/cc/06/a17e68118fda2f195ab9cd66a3e7.jpg",
        "quantity": "500.0",
        "measure_unit": "g",
        "description": "Kalas",
        "category": "Condimente si Sosuri",
        "price": 11.5,
        "reviews": null,
        "rating": null
    }]
    }


    return existing_products_list.get(recipe_name)