# Zinobe Prueba

Obtener un listado de países y regiones desde  https://restcountries.eu/ y https://rapidapi.com/apilayernet/api/rest-countries-v1,
Contabilizar el tiempo procesado.
Guardar el resultado en sqlite, en JSON File y en MongoDB.

##Solución del ejercicio:

En la carpeta raíz del proyecto se encuentra el ETL que obtiene los datos de regiones y países. Dicho ETL guarda en JSON File, Mongo y SQLlite el resultado.

Posteriormente en la carpeta zinobeapi se encuentra el servicio web que emula el comportamiento de OAUTH2 para autenticar y visualizar las regiones obtenidas.

## Instalación.

1. Obtener la imagen de Mongo.

```
docker run -d -p 27017:27017 --name m1 mongo
```

2. Construir imagen ETL
```
cd zinobeetl && docker build -t zinobeetl . 
```

3. Construir imagen API
```
cd zinobeapi && docker build -t zinobeapi . 
```