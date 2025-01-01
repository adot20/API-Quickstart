import requests

def fetch_random_user_data_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        user_country = user_data["location"]["country"]
        return username, user_country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username, user_country = fetch_random_user_data_freeapi()
        print(f"Username: {username} \nCountry: {user_country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()