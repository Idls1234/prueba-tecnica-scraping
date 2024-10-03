# Prueba tecnica scraping

_api creada en python3/flask/BeautifulSoup/playwright para webscraping_

### Librerias utilizadas🔧
* beautifulsoup4 
* flask 
* requests
* docker
* playwright

### Correr el proyecto⚙️

_Crear imagen docker_
```sh
#correr el siguiente comando en la carpeta del proyecto
docker build -t pruebatecnica-api .
```


_Ejecutar imagen generada_
```sh
docker run -d -p 8000:8000 pruebatecnica-api
```

## Como utilizar el proyecto💡

_Endpoints disponibles_

| tipo      | endpoint                      | descripcion                                                   |
| --------- | ---------                     | ---------                                                     |
| GET       | localhost:8000/prueba1        | Procesa el JSON de la prueba y descarga un archivo en formato CSV.|
| POST      | localhost:8000/prueba2        | Obtiene los productos mediante web scraping de la URL proporcionada.enviada                    |

_Comandos CURL para prueba de poyecto_ 
```sh
#prueba 1
curl --location --request GET 'http://127.0.0.1:8000/prueba1' \
--header 'Content-Type: application/json'

#prueba 2
curl --location 'http://127.0.0.1:8000/prueba2' \
--header 'Content-Type: application/json' \
--data '{
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas"
}'
```

## Notas🗒️

* Al hacer clic en el ejemplo de la salida esperada en el PDF, se redirige a un archivo .js en lugar de un archivo .json.

* En el archivo CSV de ejemplo de la prueba 1, los valores de unit_size y net_weight son iguales. En los datos proporcionados para la prueba, el producto no tiene un valor para unit_size. Se ha agregado una validación para que, si unit_size no tiene valor, se asigne el valor de net_weight.

* Las paginas de la prueba 2 son de contenido dinamico js. toma algo de tiempo el request ya que la informacion al ser dinamica tarda en cargarse.