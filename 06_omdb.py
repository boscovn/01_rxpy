import requests
import rx
from printer import Printer
params = {
    'apikey': 'd3f6dabf',
    's': input('Película a buscar: ')
}

content = requests.get(f'http://www.omdbapi.com/', params=params)

data = content.json()
#todo ejercicio
rx.from_(data['Search']).pipe(

).subscribe(Printer())