from jsonModules import json_data
def calculate_xp(recipe_index, user_time_minutes, image_compare_score):
    total_time = json_data(recipe_index, "prepTimeMinutes") + json_data(recipe_index, "cookTimeMinutes")
    time_grade, image_grade, grade_mult, image_bonus = None, None, None, None
    time_score = (total_time / user_time_minutes)*100
    difficulty = json_data(recipe_index, "difficulty")
    print(difficulty)
    match image_compare_score:
        case a if 90 <= a <= 100 or a > 100:
            image_grade = "A"
            image_bonus = 50
        case b if 80 <= b <= 89:
            image_grade = "B"
            image_bonus = 40
        case c if 70 <= c <= 79:
            image_grade = "C"
            image_bonus = 30
        case d if 60 <= d <= 69:
            image_grade = "D"
            image_bonus = 20
        case f if f <= 49:
            image_grade = "F"
            image_bonus = 10
        case _:
            print("Invalid value in param image_compare_score")
            exit()
    if difficulty == "Easy":
        base_xp = total_time+image_bonus
    elif difficulty == "Medium":
        base_xp = 2*(total_time+image_bonus)
    elif difficulty == "Hard":
        base_xp = 3*(total_time+image_bonus)
    else:
        print("Invalid difficulty. make sure recipe_index is a valid index for all_recipes.json")
        exit()
    match time_score:
        case a if 90 <= a <= 100 or a > 100:
            time_grade = "A"
            grade_mult = 1.5
        case b if 80 <= b <= 89:
            time_grade = "B"
            grade_mult = 1.25
        case c if 70 <= c <= 79:
            time_grade = "C"
            grade_mult = 1
        case d if 60 <= d <= 69:
            time_grade = "D"
            grade_mult = 0.75
        case f if f <= 49:
            time_grade = "F"
            grade_mult = 0.5
        case _:
            print("Invalid time in calculate_xp.")
            exit()
    total_xp = base_xp * grade_mult
    return total_xp, time_grade, image_grade,
