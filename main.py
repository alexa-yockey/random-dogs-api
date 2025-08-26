import requests 

if __name__ == "__main__":
    url = "https://dog.ceo/api/breeds/image/random"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()
        print(data)

    except requests.exceptions.RequestException as e:
        print("Something went wrong with the API call:", e)