![mooc](https://github.com/Rominagarcia/MachineLearning/assets/96449858/2ac92855-dd98-472d-8875-4aff17e5cab3)

# Proyecto individual N°1 | Machine Learning

*Desarrollado por García Romina Giselle*

**Descripción**
Este proyecto representa mi contribución como Data Scientist en una start-up especializada en servicios de agregación de plataformas de streaming. Para cumplir con los requisitos del proyecto, se me proporcionaron dos archivos en formato .CSV que contienen datos detallados sobre películas transmitidas en la plataforma.

**El proyecto se centra en los siguientes objetivos:**
Realizar consultas específicas a los datos para obtener información relevante.
Crear un modelo de recomendación de películas capaz de ofrecer una lista de 5 películas similares al ingresar un título.
Desarrollar una API que exponga las funcionalidades mencionadas anteriormente y permita su fácil integración y consumo.

**Incluye las siguientes consultas a los datos:**
- *peliculas_idioma:* Devuelve la cantidad de películas producidas en el idioma especificado.
- *peliculas_duracion:* Proporciona la duración y el año de lanzamiento de una película específica.
- *franquicia:* Muestra la cantidad de películas, las ganancias totales y el promedio de una franquicia específica.
- *peliculas_pais:* Ofrece la cantidad de películas producidas en un país específico.
- *productoras_exitosas:* Informa sobre las ganancias totales y la cantidad de películas realizadas por una productora específica.
- *recomendacion(titulo):* Recibe el título de una película y proporciona una lista de las 5 películas más similares.

**Modelo de Recomendación de Películas**
Este proyecto implementa un modelo de recomendación de películas basado en contenido. Utilizando técnicas de aprendizaje automático, el modelo procesa información clave, como el título, género, actores y directores de las películas, para encontrar aquellas que sean similares.

**El flujo de trabajo del proyecto se divide en los siguientes pasos:**
*Preprocesamiento de datos:* Se realiza una limpieza y transformación de los datos para asegurar su calidad y adecuación al modelo.
*Creación de una matriz de características:* Se generan vectores de características para cada película en los datos, describiendo de manera precisa sus atributos.
*Cálculo de similitudes:* Se utiliza la medida de similitud del coseno para calcular la similitud entre los vectores de características de las películas.
*Recomendación de películas:* Se seleccionan las 5 películas más similares al título proporcionado como parámetro y se presentan como resultado de la recomendación.

**Conclusiones:**

**Implementación/Uso**
- En el archivo ETL.ipynb se encuentra todo lo referido a el proceso de transformacion de los datos crudos que nos proporcionan. Para mas info remitirse a dicho archivo.
- En el archivo EDA.ipynb se encuentra el Analisis Exploratorio de Datos(EDA). Para mas info remitirse a dicho archivo.
- En el archivo main.py se encuentra el achivo principal, el cual se deve ejecutar en la API.
- Link donde se puede acceder a la API >> [API](https://machinelearningrominagisellegarcia.onrender.com).
- Link donde ejecutar los comandos de la API >> [API/Docs](https://machinelearningrominagisellegarcia.onrender.com/docs).

### *Bibliografía*
Consignas del Proyecto >> [Archivo](https://github.com/soyHenry/PI_ML_OPS/blob/main/Readme.md).
