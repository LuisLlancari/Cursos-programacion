import requests

r = requests.get("https://pokeapi.co/api/v2/region")

if r.status_code == 200:
    data = r.json()

    resultados = data['results']

    for i in resultados:
        print(i['name'])

else:
    print("error:", r.status_code)
