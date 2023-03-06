import requests, json

image_url = 'https://www.kivano.kg/images/product/114889/1670556729_45777900.jpg'

response = requests.get(image_url)

with open("images/test.jpg", "wb") as file:
    file.write(response.content)
