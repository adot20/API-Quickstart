import requests
import random

def fetch_random_sayings():
    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    response = requests.get(url)
    data = response.json()

    if data["success"]:
        quote_data = data["data"]["data"]
        random_quote = random.choice(quote_data)
        wisdom_word = random_quote["content"]
        author = random_quote["author"]
        return wisdom_word, author
    else:
        raise Exception("Failed to fetch quote data")

def main():
    try:
        wisdom_word, author = fetch_random_sayings()
        print(f"{wisdom_word} - {author}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()