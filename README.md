# Prueba tecnica scraping

_api creada en python3/fastapi/BeautifulSoup para webscraping_

### Librerias utilizadas🔧
* beautifulsoup4 
* fastapi 
* uvicorn 
* requests
* docker
* openapi

### Correr el proyecto⚙️

_Crear imagen docker_
```
#correr el siguiente comando en la carpeta del proyecto
docker build -t pruebatecnica-api .
```


_Ejecutar imagen generada_
```
docker run -d -p 8000:8000 pruebatecnica-api
```

## Como utilizar el proyecto💡
El proyecto utiliza FastAPI, que incluye el estándar OpenAPI. Esto facilita la prueba de los endpoints de la API. Para acceder a la documentación y probar los endpoints, visita la siguiente URL: http://127.0.0.1:8000/docs


_Endpoints disponibles_

| tipo      | endpoint              | descripcion                                                   |
| --------- | ---------             | ---------                                                     |
| GET       | /prueba1              | Procesa el JSON de la prueba y descarga un archivo en formato CSV.|
| POST      | /prueba2              | Obtiene los productos mediante web scraping de la URL proporcionada.enviada                    |


## Notas🗒️

* Al hacer clic en el ejemplo de la salida esperada en el PDF, se redirige a un archivo .js en lugar de un archivo .json.

* En el archivo CSV de ejemplo de la prueba 1, los valores de unit_size y net_weight son iguales. En los datos proporcionados para la prueba, el producto no tiene un valor para unit_size. Se ha agregado una validación para que, si unit_size no tiene valor, se asigne el valor de net_weight.