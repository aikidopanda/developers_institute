import requests
from time import time

def time_to_load(website) -> str:
    response = requests.get(website).elapsed.total_seconds()
    return response

#Testing
print(time_to_load('http://google.com'))
print(time_to_load('http://imdb.com'))
print(time_to_load('http://learn.di-learning.com/'))


