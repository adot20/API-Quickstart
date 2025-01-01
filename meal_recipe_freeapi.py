import requests
import random

def fetch_random_meal_data():
    url = "https://api.freeapi.app/api/v1/public/meals?page=1&limit=10"
    result = requests.get(url)
    data = result.json()
    
    if data["success"] and "data" in data:
        meal_data = data["data"]["data"]
        random_meal = random.choice(meal_data)
        meal_name = random_meal["strMeal"]
        meal_insruction = meal_data[1]["strInstructions"]
        return meal_name, meal_insruction
    else:
        raise Exception("Failed to fetch meal data")

def main():
    try:
        meal_name, meal_instruction = fetch_random_meal_data()
        print(f"Dish: {meal_name} \nInstruction to follow: {meal_instruction}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()