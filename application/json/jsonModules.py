import json
def json_data(recipe_index,returned_obj):
    json_file = open('APIs/all_recipes.json', "r")
    full_recipe_dict = json.load(json_file)
    try:
        selected_data = full_recipe_dict["recipes"][recipe_index][returned_obj]
        return selected_data
    except IndexError:
        print(f"Recipe index: {recipe_index} is out of range. enter an integer value between 1-49.")
    except KeyError:
        print(f"Recipe object: {returned_obj} doesn't exist.")