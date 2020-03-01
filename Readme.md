# Zinobe Prueba

Obtener un listado de países y regiones desde  https://restcountries.eu/ y https://rapidapi.com/apilayernet/api/rest-countries-v1,
Contabilizar el tiempo procesado.
Guardar el resultado en sqlite, en JSON File y en MongoDB.

## Solución del ejercicio:

En la carpeta raíz del proyecto se encuentra el ETL que obtiene los datos de regiones y países. Dicho ETL guarda en JSON File, Mongo y SQLlite el resultado.

Posteriormente en la carpeta zinobeapi se encuentra el servicio web que emula el comportamiento de OAUTH2 para autenticar y visualizar las regiones obtenidas.

## Instalación.

Para instalar únicamente se debe ejecutar el comando

```
docker-compose up
```

## Autenticacion OAUTH2

El API dispone de dos end points que son usados para emular OAUTH2. Para esto se debe consumir de la siguiente forma.

1. Obtener un token:
```
curl --location --request POST '127.0.0.1:5000/api/token/' \
--header 'Content-Type: multipart/form-data; boundary=--------------------------059353707752847917006718' \
--form 'owner=admin@zinobe.com'
```

2. Acceder al servidor de recursos:
```
curl --location --request GET '127.0.0.1:5000/api/regions/' \
--header 'owner: admin@zinobe.com' \
--header 'token: TOKEN_STRING'
```