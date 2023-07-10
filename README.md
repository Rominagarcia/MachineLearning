# Proyecto individual N°1 - Machine Learning Operations (MLOps)

*Desarrollado por Romina Giselle García*

*El proyecto consiste en trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming.
Para ello nos entregan dos archivos .CSV en crudo con los datos de peliculas que emiten en la plataforma.*

## *Requisitos*
- Realizar ciertas consultas a los datos.
- Realizar un modelo de recomendacion de peliculas que al ingresar un titulo nos devuelva una recomendacion de 5 peliculas similares.
- Realizar una API lista para su consumo con los puntos anteriores.

## *Consulta de Datos*
- cantidad_filmaciones_mes: Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
- cantidad_filmaciones_dia: Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
- score_titulo: Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
- votos_titulo: Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
- get_actor: Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
- get_director: Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.


## *Modelo de recomendación de películas*
Este proyecto realiza un modelo de recomendación de películas basado en contenido. Este tipo de modelo utiliza información sobre las películas, como su título, género, actores y directores, para encontrar películas similares.

## *Una vez que se tiene la fuente de datos, se realizan los siguientes pasos:*
- Preprocesamiento de datos: Se limpian los datos y transforman en un formato adecuado para el modelo.
- Creación de una matriz de características: Para cada película en la fuente de datos, se crea un vector de características que describa la película.
- Cálculo de similitudes: Para encontrar películas similares, se calcula la similitud entre los vectores de características de todas las películas en la fuente de datos. Para ello se utiliza la similitud del coseno.
- Recomendación de películas: Se encuentran las 5 películas más similares al título recibido como parámetro y se lo muestra en una lista.

### *Implementación/Uso*
- En el archivo ETL.ipynb se encuentra todo lo referido a el proceso de transformacion de los datos crudos que nos proporcionan. Para mas info remitirse a dicho archivo.
- En el archivo EDA.ipynb se encuentra el Analisis Exploratorio de Datos(EDA). Para mas info remitirse a dicho archivo.
- En el archivo main.py se encuentra el achivo principal, el cual se deve ejecutar en la API.
- Link donde se puede acceder a la API >> [API] (https://individualprojectrominagiselle.onrender.com).
- Link donde ejecutar los comandos de la API >> [API/Docs] (https://individualprojectrominagiselle.onrender.com/docs).

### *Bibliografía*
Consignas del Proyecto >> [Archivo] (https://github.com/HX-PRomero/PI_ML_OPS/blob/main/Readme.md). 
