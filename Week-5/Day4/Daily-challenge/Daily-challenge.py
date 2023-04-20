import requests
import random
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '#'
DATABASE = 'Home'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)
# cursor = connection.cursor()

url = 'https://restcountries.com/v3.1/all'

response = requests.get(url)
# print(response.json())

def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_random_instances(data_list, n):
    instances = []
    for _ in range(n):
        random_inst = random.choice(data_list)
        instances.append(random_inst)
    return instances

def extract(instance: dict):
    try:
        name = instance['name']['common']
        capital = instance['capital'][0]
        flag = instance['flag']
        subregion = instance['subregion']
        population = instance['population']

        return name, capital, flag, subregion, population
    
    except KeyError:
        return None


def preprocess(instances: list):

    preprocessed = []

    for instance in instances:
        preprocessed_inst = extract(instance)
        # print(preprocessed_inst)
        if preprocessed_inst is None:
            continue
        preprocessed.append(preprocessed_inst)
    return preprocessed

data = get_data(url)

random_inst = get_random_instances(data, 10)

clean_instances = preprocess(random_inst)
print (clean_instances)

def insert_query(columns_names, data, table_name):
    columns = ', '.join(columns_names)
    name, capital, flag, subregion, population = data
    query = f"insert into {table_name} ({columns}) values ('{name}', '{capital}', '{flag}', '{subregion}', {population})"

    return query

columns = ['name', 'capital', 'flag', 'subregion', 'population']

def run_change_query(query: str): 
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
        print("SUCCESS")


for clean_inst in clean_instances:
    q = insert_query(columns_names=columns, data=clean_inst, table_name='countries')
    run_change_query(q)



