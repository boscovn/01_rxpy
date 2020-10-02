import requests
import rx

params = {
    'apikey': 'd3f6dabf',
    's': input('Película a buscar: ')
}

content = requests.get(f'http://www.omdbapi.com/', params=params)

data = content.json()
print(data.items())
#todo ejercicio