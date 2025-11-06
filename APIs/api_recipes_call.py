import requests
import json
import urllib.request

from flask import jsonify


def get_preload_recipes():
    url = "https://dummyjson.com/recipes?limit=10"
    response = urllib.request.urlopen(url)
    recipe_data = json.loads(response.read())

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result)

    with open('10_recipes.json', 'a') as file:
        json.dump(recipe_data, file)
        file.close()
        return result

def get_all_recipes():
    url = "https://dummyjson.com/recipes?limit=0"
    response = urllib.request.urlopen(url)
    recipe_data = json.loads(response.read())

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    print(result)

    with open('all_recipes.json', 'a') as file:
        json.dump(recipe_data, file)
        file.close()
        return result

def load_more_recipes(region):
    region = str(region)
    list_of_recipes = []
    with open('all_recipes.json', 'r') as file:
        data = json.load(file)
        for i in data['recipes']:
            if i['cuisine'] == region:
                list_of_recipes.append(i)

    print(list_of_recipes)
    file.close()


    return list_of_recipes

# will return the attributes associated with the region/cuisine.  For the list of choices to choose from.
load_more_recipes('Asian')

# "id":5,
# "name":"Mango Salsa Chicken",
# "ingredients":["Chicken thighs","Mango, diced","Red onion, finely chopped","Cilantro, chopped","Lime juice","Jalapeño, minced","Salt and pepper to taste","Cooked rice for serving"],
# "instructions":["Season chicken thighs with salt and pepper.","Grill or bake chicken until fully cooked.","In a bowl, combine diced mango, chopped red onion, cilantro, minced jalapeño, and lime juice.","Dice the cooked chicken and mix it with the mango salsa.","Serve over cooked rice."],
# "prepTimeMinutes":15,
# "cookTimeMinutes":25,
# "servings":3,
# "difficulty":"Easy",
# "cuisine":"Mexican",
# "caloriesPerServing":380,
# "tags":["Chicken","Salsa"],
# "userId":26,
# "image":"https://cdn.dummyjson.com/recipe-images/5.webp",
# "rating":4.9,
# "reviewCount":63,
# "mealType":["Dinner"]}
