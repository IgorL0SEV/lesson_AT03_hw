# get_url_CAT_IMAGE
import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный статус код
        data = response.json()
        return data[0]['url'] if data else None
    except requests.exceptions.HTTPError as http_err:
        # Обработка ошибок HTTP
        return None
    except requests.exceptions.RequestException:
        return None



#print(get_random_cat_image())