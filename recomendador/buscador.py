import tmdbsimple as tmdb
import requests
from datasets import load_dataset

ds = load_dataset("nbtpj/Movies_and_TV")

url = "https://api.themoviedb.org/3/movie/"
url_img = "https://image.tmdb.org/t/p/original"
url_imdb = "https://www.imdb.com/title/"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMzU2NjI4YzYwNTU5MThjMDBhZTczNWM0NmVjM2IxNSIsIm5iZiI6MTcyNDY5MzUyNC45NjMyNTgsInN1YiI6IjY2Y2NiYjg0ODE0YjMzM2EwYjIwNmQxZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.G9a4fLKo22B9UYc1z3gMTquMTPmFAtV7qcj3pWopalE"
}

tmdb.API_KEY = '1356628c6055918c00ae735c46ec3b15'

search = tmdb.Search()


def listar_ids(pelis):
    ids = []

    if len(pelis) > 0:
        for p in pelis:
            if not len(p) > 100:
                response = search.movie(query=p)
            if response['total_results'] > 0:
                ids.append(response['results'][0]['id'])

    return ids


def sacar_datos_pelis(pelis):
    ids = listar_ids(pelis)
    datos = []

    for i in ids:
        response = requests.get(
            f"{url}/{i}?language=es-ES", headers=headers, timeout=3)

        print(response.json())

        if response.status_code == 200:
            data = response.json()
            show_data = {"nombre": data['title'], "sinopsis": data['overview'],
                         "poster": "", "anyo": data["release_date"][0:4], "IMDB": "", "generos": [], "puntuacion": data['vote_average']}
            
    
            if data['imdb_id'] is not None:
                for g in data['genres']:
                    show_data['generos'].append(g['name'])
            
            if data['imdb_id'] is None:
                show_data['IMDB'] = ""
            else:
                show_data['IMDB'] = f"{url_imdb}{data["imdb_id"]}"

            if data['poster_path'] is None:
                show_data['poster'] = ""
            else:
                show_data['poster'] = f"{url_img}{data['poster_path']} "

            print(show_data['puntuacion'])
            datos.append(show_data)

    return datos
