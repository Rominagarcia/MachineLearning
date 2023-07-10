![mooc](https://github.com/Rominagarcia/MachineLearning/assets/96449858/2ac92855-dd98-472d-8875-4aff17e5cab3)

# Proyecto individual N°1 | Machine Learning

*Desarrollado por García Romina Giselle*

**Introducción**
Como Data Scientist en una start-up enfocada en servicios de agregación de plataformas de streaming, tuve la oportunidad de llevar a cabo un proyecto significativo que busca mejorar la comprensión y el aprovechamiento de los datos relacionados con las películas transmitidas en nuestra plataforma. En este proyecto, se me proporcionaron dos archivos en formato csv que contienen información detallada sobre las películas.

El objetivo principal de este proyecto es aprovechar el potencial de los datos para obtener información valiosa y generar recomendaciones personalizadas a nuestros usuarios. Para lograrlo, utilicé técnicas avanzadas de análisis de datos y aprendizaje automáticocon el fin de extraer patrones, tendencias y conocimientos relevantes.

El primer paso de mi proceso consistió en realizar una exploración exhaustiva de los conjuntos de datos. Mediante un enfoque riguroso, identifiqué las variables clave y realicé una limpieza y preprocesamiento de los datos para garantizar su calidad y coherencia. Además, llevé a cabo una transformación y codificación adecuada de las características pertinentes con el objetivo de preparar los datos para su posterior análisis.

Como paso siguiente, procedí a realizar un análisis descriptivo para obtener una visión general de las características de las películas en nuestra plataforma. Mediante visualizaciones y correlaciones relevantes, obtuve información detallada sobre géneros populares, calificaciones, duración y otras características relevantes para nuestro negocio.

Para ofrecer recomendaciones personalizadas a nuestros usuarios, implementé un modelo que tiene como objetivo ofrecer recomendaciones personalizadas a nuestros usuarios.

Utilicé técnicas avanzadas de aprendizaje automático para desarrollar y entrenar un modelo que procesa información clave sobre las películas, como el título. Esta información se utiliza para encontrar películas similares y proporcionar recomendaciones personalizadas a cada usuario, teniendo en cuenta sus preferencias individuales.

El modelo de recomendación basado en contenido aprovecha los patrones y las características intrínsecas de las películas para establecer relaciones de similitud. Al analizar en detalle las características mencionadas anteriormente, el modelo identifica aquellas películas que comparten características similares y las sugiere a los usuarios en función de sus preferencias.

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
