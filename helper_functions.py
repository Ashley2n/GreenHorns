import json
import os

from cryptography.fernet import Fernet


def load_key() -> bytes:
    _key_file = 'key.txt'

    if os.path.exists(_key_file):
        with open(_key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(_key_file, 'wb') as f:
            f.write(key)

    return key


def encrypt_password(password: str) -> bytes:
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password: bytes) -> str:
    return fernet.decrypt(encrypted_password).decode()



fernet = Fernet(load_key())

def get_json_data_recipe(recipe_index,returned_obj):
    json_file = open('APIs/all_recipes.json', "r")
    full_recipe_dict = json.load(json_file)
    try:
        selected_data = full_recipe_dict["recipes"][recipe_index][returned_obj]
        return selected_data
    except IndexError:
        print(f"Recipe index: {recipe_index} is out of range. enter an integer value between 0 through 49.")
    except KeyError:
        print(f"Recipe object: {returned_obj} doesn't exist.")

# print(get_json_data_recipe(2,"name"))
#
# print(get_json_data_recipe(80,"difficulty"))

def game_screen_data(index):
    return {
        "name": get_json_data_recipe(index, "name"),
        "prep_time": get_json_data_recipe(index, "prepTimeMinutes"),
        "cookTimeMinutes": get_json_data_recipe(index, "cookTimeMinutes"),
        "instructions" : get_json_data_recipe(index, "instructions"),
        "ingredients" : get_json_data_recipe(index,'ingredients'),
        "servings": get_json_data_recipe(index, "servings"),
        "difficulty" : get_json_data_recipe(index, "difficulty"),
        "cuisine": get_json_data_recipe(index, "cuisine"),
        "caloriesPerServing": get_json_data_recipe(index, "caloriesPerServing"),
        "rating": get_json_data_recipe(index, "rating"),
        "mealType" : get_json_data_recipe(index, "mealType")[0]
    }

def get_recipe_image(recipe_index):
    return {
        'image_url' : get_json_data_recipe(recipe_index, "image"),
    }