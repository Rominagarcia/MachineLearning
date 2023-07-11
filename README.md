![mooc](https://github.com/Rominagarcia/MachineLearning/assets/96449858/2ac92855-dd98-472d-8875-4aff17e5cab3)

# Proyecto individual N°1  
###  Machine Learning

*Desarrollado por García Romina Giselle*

## **Introducción**
Como Data Scientist en una start-up enfocada en servicios de agregación de plataformas de streaming, tuve la oportunidad de llevar a cabo un proyecto significativo que busca mejorar la comprensión y el aprovechamiento de los datos relacionados con las películas transmitidas en nuestra plataforma. En este proyecto, se me proporcionaron dos archivos en formato csv que contienen información detallada sobre las películas.

> El objetivo principal de este proyecto es aprovechar el potencial de los datos para obtener información valiosa y generar recomendaciones personalizadas a nuestros usuarios. Para lograrlo, utilicé técnicas avanzadas de análisis de datos y aprendizaje automático con el fin de extraer patrones, tendencias y conocimientos relevantes.

El primer paso de mi proceso consistió en realizar una exploración exhaustiva del conjunto de datos. Mediante un enfoque riguroso, identifiqué las variables clave y realicé una limpieza y preprocesamiento de los datos para garantizar su calidad y coherencia. Además, llevé a cabo una transformación y codificación adecuada de las características pertinentes con el objetivo de preparar los datos para su posterior análisis.

Como paso siguiente, procedí a realizar un análisis descriptivo para obtener una visión general de las características de las películas en nuestra plataforma. Mediante visualizaciones y correlaciones relevantes, obtuve información detallada sobre géneros populares, duración y otras características relevantes para nuestro negocio.

Para ofrecer recomendaciones personalizadas a los usuarios, implementé un modelo que tiene como objetivo ofrecer recomendaciones personalizadas a los mismos. Utilicé técnicas avanzadas de aprendizaje automático para desarrollar y entrenar un modelo que procesa información clave sobre las películas, como el título. Esta información se utiliza para encontrar películas similares y *proporcionar recomendaciones personalizadas a cada usuario, teniendo en cuenta sus preferencias individuales.*

El modelo de recomendación basado en contenido aprovecha los patrones y las características intrínsecas de las películas para establecer relaciones de similitud. Al analizar en detalle las características mencionadas anteriormente, el modelo identifica aquellas películas que comparten características similares y las sugiere a los usuarios en función de sus preferencias.

## **Flujo de trabajo**

### **Preprocesamiento de datos** 
En esta etapa, se realiza una limpieza y transformación de los datos para asegurar su calidad y adecuación al modelo. Esto implica la eliminación de valores faltantes, la normalización de datos, la codificación adecuada de variables categóricas y cualquier otra tarea necesaria para garantizar que los datos sean coherentes y aptos para el análisis.

### **Análisis Exploratorio de Datos (EDA)** 
Es una etapa crítica en cualquier proyecto de análisis de datos. Consiste en investigar y comprender la información en bruto mediante técnicas estadísticas y visuales. El EDA ayuda a revelar patrones, tendencias, distribuciones y posibles relaciones entre las variables presentes en los datos.

### **1) Descripción de los datos** 
Se examinan las características de las variables, como su tipo (numérico, categórico), la cantidad de valores faltantes, la distribución de los valores y los posibles outliers (valores atípicos). También se exploran las relaciones entre las variables.

### **2) Visualización de los datos** 
Se utilizan gráficos y visualizaciones adecuadas como gráficos de barras y gráficos circulares, para comprender la distribución y las relaciones entre las variables. Estas visualizaciones ayudan a identificar patrones, valores atípicos y posibles correlaciones.

### **3) Análisis de correlación** 
Se examina la correlación entre las variables para identificar posibles relaciones lineales o no lineales. Esto puede ayudar a determinar qué variables pueden ser relevantes para el modelo y cómo interactúan entre sí.

### **4) Identificación de valores atípicos** 
Se buscan valores que se desvíen significativamente de la tendencia general de los datos. Pueden requerir una atención especial para comprender su origen y determinar si deben ser tratados o excluidos en el análisis.

### **Creación de una matriz de características** 
Una vez que los datos han sido preprocesados, se procede a generar vectores de características para cada película en los datos. Estos vectores describen de manera precisa los atributos relevantes de cada película, como el título, género y directores. Cada película se representa mediante un vector numérico que captura su información clave.

### **Cálculo de similitudes**
Utilizando la medida de similitud del coseno, se calcula la similitud entre los vectores de características de las películas. Esto implica comparar la proximidad de las películas en función de sus características compartidas. Cuanto más cercanos sean los vectores, mayor será la similitud entre las películas.

### **Recomendación de películas** 
Con base en el cálculo de similitudes, se seleccionan las 5 películas más similares al título proporcionado como parámetro. Se eligen en función de su similitud con la película ingresada, utilizando la medida de similitud previamente calculada. El resultado de esta etapa es una lista de las películas más similares, que se presentan como resultado de la recomendación al usuario.

## **El proyecto se centra en los siguientes objetivos**

- ### **Realizar consultas específicas a los datos para obtener información relevante** 
Se busca explorar y analizar los conjuntos de datos proporcionados mediante consultas específicas que nos permitan obtener información relevante sobre las películas transmitidas en nuestra plataforma de agregación de streaming. Estas nos ayudarán a identificar patrones, tendencias y características clave que nos brinden una comprensión profunda del contenido disponible.

- ### **Crear un modelo de recomendación de películas capaz de ofrecer una lista de 5 películas similares al ingresar un título** 
Uno de los objetivos principales del proyecto es desarrollar un modelo de recomendación basado en contenido que pueda generar recomendaciones personalizadas para nuestros usuarios. Este modelo utilizará técnicas de aprendizaje automático para procesar información clave, como el título de las películas, y proporcionará una lista de 5 películas similares a aquella ingresada por el usuario. Estas recomendaciones se basarán en las características compartidas entre las películas para garantizar una experiencia personalizada y relevante para cada usuario.

- ### **Desarrollar una API que exponga las funcionalidades mencionadas anteriormente y permita su fácil integración y consumo** 
Para asegurar la accesibilidad y la integración de las funcionalidades desarrolladas, se creará una API que expondrá las consultas específicas a los datos y el modelo de recomendación de películas. Esta API permitirá a otros sistemas y aplicaciones utilizar y consumir estas funcionalidades de manera eficiente. Estará diseñada para ser intuitiva, documentada adecuadamente y contar con las mejores prácticas de seguridad.

## **Las consultas fundamentales en las que me centré son las siguientes**
- *peliculas_idioma:* Esta consulta devuelve la cantidad de películas producidas en el idioma especificado. Permite obtener una visión cuantitativa de las películas disponibles en nuestra plataforma en relación con los idiomas de producción. Al ejecutar esta consulta, se obtendrá un recuento de las películas producidas en el idioma seleccionado.

- *peliculas_duracion:* Proporciona la duración y el año de lanzamiento de una película específica. Al ingresar el título de una película, esta consulta nos brindará información detallada sobre su duración y el año en que se lanzó. Esto resulta útil para conocer detalles específicos sobre una película en particular.

- *franquicia:* Mediante esta consulta, se muestra la cantidad de películas, las ganancias totales y el promedio de una franquicia específica. Al ingresar el nombre de una franquicia, obtendremos información detallada sobre el número total de películas que la componen, las ganancias acumuladas de todas las películas de la franquicia y el promedio de ganancias por película.

- *peliculas_pais:* Esta consulta ofrece la cantidad de películas producidas en un país específico. Al especificar un país, obtendremos el recuento de películas producidas en ese país en particular. Esta información puede ser útil para comprender la distribución geográfica de las producciones cinematográficas en nuestra plataforma.

- *productoras_exitosas:* Informa sobre las ganancias totales y la cantidad de películas realizadas por una productora específica. Al ingresar el nombre de una productora, obtendremos detalles sobre las ganancias totales generadas por las películas producidas por esa productora, así como el recuento de películas en su cartera.

## **Modelo de Machine Learning**
- *recomendacion:* Esta consulta recibe el título de una película y proporciona una lista de las 5 películas más similares. Al ejecutar esta consulta, utilizando técnicas de recomendación basada en contenido, se generará una lista de las películas que comparten características similares con la película ingresada. Estas recomendaciones ayudarán a nuestros usuarios a descubrir y explorar películas afines a sus preferencias.

## **Conclusiones:**
Luego de completar el análisis de datos y el desarrollo del modelo de recomendación de películas, los resultados corroboraron de forma positiva cada uno de los objetivos establecidos. El análisis de datos proporcionó información relevante y detallada sobre las películas transmitidas en la plataforma de agregación de streaming, permitiendo identificar patrones, tendencias y características clave que brindaron una comprensión profunda del contenido disponible. Esto demostró que las consultas específicas a los datos fueron efectivas para obtener información relevante.

En cuanto al modelo de recomendación de películas, se logró crear un sistema capaz de ofrecer una lista de 5 películas similares al ingresar un título. Utilizó técnicas de aprendizaje automático y se basó en características compartidas entre las películas para garantizar una experiencia personalizada y relevante para cada usuario. Estos resultados confirmaron el éxito del objetivo de ofrecer recomendaciones personalizadas, brindando a los usuarios una experiencia mejorada y adaptada a sus gustos y preferencias.

Además, se desarrolló una API que expone las funcionalidades mencionadas anteriormente, permitiendo su fácil integración y consumo por parte de otros sistemas y aplicaciones. Esta API fue diseñada de manera intuitiva, documentada adecuadamente y siguiendo las mejores prácticas de seguridad, lo que facilita su implementación y utilización por parte de terceros.

> *En conclusión, los objetivos del proyecto fueron cumplidos de manera satisfactoria. El análisis de datos brindó información valiosa, el modelo de recomendación personalizada cumplió con las expectativas y la API desarrollada permite una fácil integración de las funcionalidades en otros sistemas. Se ha logrado llevar a cabo una personalización en la experiencia del usuario, brindándole recomendaciones acordes a sus gustos y preferencias. Esto refuerza la idea de que el consumidor ocupa un lugar central en el proyecto y se le ofrece un servicio que busca satisfacer sus necesidades y preferencias. A través de este análisis, se ha logrado aportar valor y mejorar la experiencia del usuario, y juntos se puede seguir trabajando para ofrecer un servicio aún mejor.*

## **Implementación/Uso**
- En el archivo ETL.ipynb se encuentra todo lo referido a el proceso de transformacion de los datos crudos que nos proporcionan. Para mas info remitirse a dicho archivo.
- En el archivo EDA.ipynb se encuentra el Analisis Exploratorio de Datos(EDA). Para mas info remitirse a dicho archivo.
- En el archivo main.py se encuentra el achivo principal, el cual se deve ejecutar en la API.
- Link donde se puede acceder a la API >> [API](https://machinelearningrominagisellegarcia.onrender.com).
- Link donde ejecutar los comandos de la API >> [API/Docs](https://machinelearningrominagisellegarcia.onrender.com/docs).
- Link para ingresar al video >> [YouTube](https://).

## *Bibliografía*
Consignas del Proyecto >> [Archivo](https://github.com/soyHenry/PI_ML_OPS/blob/main/Readme.md).
