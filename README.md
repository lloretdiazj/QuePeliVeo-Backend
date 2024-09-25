# QuePeliVeo-Backend
## Descripción

Esta es la parte backend de la herramienta para recomendar películas QuePeliVeo, aquí es donde se encuentra la mayor parte de la lógica de la aplicación, la cual esta codificada en Python usando las librerías openai, tmdbsimple y flask.

Para el correcto funcionamiento de la aplicación es necesario tener instalado LM Studio, se está planteando cambiar a otra alternativa si se llegara a desplegar la app.

## Endpoint GET /recomendador

Este endpoint permite obtener recomendaciones de películas basadas en un prompt y un número específico de resultados.

</br>
    <table>
        <thead>
            <tr>
                <th>Parámetro</th>
                <th>Tipo</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>prompt</td>
                <td>string</td>
                <td>El prompt o tema sobre el cual se desean recomendaciones (e.j., "miedo y terror").</td>
            </tr>
            <tr>
                <td>numero</td>
                <td>int</td>
                <td>El número de recomendaciones deseadas.</td>
            </tr>
        </tbody>
    </table>

## Ejemplo de uso
<p>http://localhost:5000/recomendador?prompt=miedo%20y%20terror&numero=2</p>

```JSON
[
    {
        "IMDB": "https://www.imdb.com/title/tt0464141",
        "anyo": "2007",
        "generos": [
            "Terror",
            "Drama",
            "Suspense"
        ],
        "nombre": "El orfanato",
        "poster": "https://image.tmdb.org/t/p/original/wk95EOzZKd74NFzVVkHBo1UW46o.jpg ",
        "puntuacion": 7.231,
        "sinopsis": "Laura regresa con su familia al orfanato en el que creció de niña, con la intenció de abrir una residencia para niños discapacitados. El nuevo entorno despierta la imaginació de su hijo, que comienza a dejarse llevar por juegos de fantasía cada vez más intensos. Éstos van inquietando a Laura cada vez más, hasta el punto en el que llega a pensar que hay algo en la casa que está amenazando a su familia. A ella le ocurre algo extraordinario y, a pesar de que es una mujer con unos principios muy claros, su universo se tambalea poniendo en duda todo aquello en lo que creía..."
    },
    {
        "IMDB": "https://www.imdb.com/title/tt0082846",
        "anyo": "1981",
        "generos": [
            "Drama",
            "Romance"
        ],
        "nombre": "En el estanque dorado",
        "poster": "https://image.tmdb.org/t/p/original/tS5Y4IAieLY3dTRJOHGaNNYwiXv.jpg ",
        "puntuacion": 7.2,
        "sinopsis": "Ethel y Norman Thayer son un anciano matrimonio que pasa sus vacaciones en un paradisiaco lugar llamado 'El Estanque Dorado'. Norman, de carácter activo, sufre con mal genio las limitaciones de la vejez y la cercanía de la muerte. Al estanque llega la hija de los Thayer, Chelsea, que mantiene una mala relación con Norman."
    }
]
```