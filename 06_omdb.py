import requests
from rx import from_, operators
from printer import Printer
params = {
    'apikey': 'd3f6dabf',
    's': input('Película a buscar: ')
}

content = requests.get(f'http://www.omdbapi.com/', params=params)

data = content.json()
from_(data['Search']).pipe(
    operators.filter(lambda t: t['Type'] == 'movie')
).subscribe(Printer())