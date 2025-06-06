import requests
from config import  BASE_URL, API_KEY

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

# Function for getting card
def get_card_data(card_id):
    response = requests.get(f"{BASE_URL}/cards/{card_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Function for getting card's comments
def get_card_comments(card_id):
    response = requests.get(f"{BASE_URL}/cards/{card_id}/comments", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Impossible to get comments:", response.status_code, response.text)
        return []

# function for getting children cards
def get_child_cards(card_id):
    response = requests.get(f"{BASE_URL}/cards/{card_id}/children", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Impossible to get connected cards:", response.status_code, response.text)
        return []