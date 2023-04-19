import requests
import random

api_url = 'https://restcountries.com/v3.1/all'
api_capital_url = 'https://restcountries.com/v3.1/capital'

response = requests.get(api_url)
# print(response.json())

rand = random.choice(response.json())
# print(rand)
print(rand['name']['common'])
print(rand['capitalInfo'])
print(rand['flags'])

response_capital = requests.get(api_capital_url)
