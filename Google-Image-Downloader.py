import requests
import os

# Replace 'your_api_key' and 'your_cse_id' with your actual API key and CSE ID
API_KEY = 'AIzaSyCBTzpJ_cwvUdXuQvlzUdtZFre9LXJBaoc'
CSE_ID = 'e15584accc8924523'


def google_search(query, api_key, cse_id, **kwargs):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'cx': cse_id,
        'key': api_key,
        'searchType': 'image',
        'num': 1,
        'safe': 'off'
    }
    params.update(kwargs)
    response = requests.get(search_url, params=params)
    result = response.json()
    return result['items']


def download_image(url, filepath):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to retrieve image.")


if __name__ == '__main__':
    query = input("Enter search query for images: ")
    results = google_search(query, API_KEY, CSE_ID)

    if results:
        image_url = results[0]['link']
        image_path = os.path.join('downloaded_images', query + '.jpg')
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        download_image(image_url, image_path)
        print(f"Image downloaded to {image_path}")
    else:
        print("No results found.")


