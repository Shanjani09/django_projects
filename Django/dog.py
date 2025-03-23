import requests as req
url = "https://dog.ceo/api/breeds/image/random"
response = req.get(url)
if response.status_code == 200:
    breed_data = response.json()
    print(breed_data['message'])
else:
    print("Error fetching image.")