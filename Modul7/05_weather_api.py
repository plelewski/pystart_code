from requests import get

url = 'https://danepubliczne.imgw.pl/api/data/synop'
cities = ['Toruń', 'Warszawa']
response = get(url)
data = response.json()
for city in data:
    if city['stacja'] in cities:
        print(city['stacja'], 'temperatura na godzinę', city['godzina_pomiaru'], 'wynosiła', city['temperatura'])
