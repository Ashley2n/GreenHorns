from jsonModules import json_data
def calculate_xp(recipe_index, user_time_minutes):
    total_time = json_data(recipe_index, "prepTimeMinutes") + json_data(recipe_index, "cookTimeMinutes")
    time_score = (total_time / user_time_minutes)*100
    difficulty = json_data(recipe_index, "difficulty")
    print(difficulty)
    if difficulty == "Easy":
        base_xp = total_time
    elif difficulty == "Medium":
        base_xp = 2*total_time
    elif difficulty == "Hard":
        base_xp = 3*total_time
    else:
        print("Invalid difficulty in calculate_xp.")
        exit()
    if 90 <= time_score >= 100:
        grade = "A"
        grade_mult = 1.5
    elif 80 <= time_score <= 89:
        grade = "B"
        grade_mult = 1.25
    elif 70 <= time_score <= 79:
        grade = "C"
        grade_mult = 1
    elif 60 <= time_score <= 69:
        grade = "D"
        grade_mult = 0.75
    elif time_score <= 49:
        grade = "F"
        grade_mult = 0.5
    else:
        print("Invalid time in calculate_xp.")
        exit()
    total_xp = base_xp * grade_mult
    return total_xp, grade
