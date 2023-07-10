#Importo las librerías que voy a utilizar para realizar cada una de las funciones
from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
import ast
from datetime import datetime
import locale #importaciones ok
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()
#http://127.0.0.1:8000

#Cargo el dataframe con los datos para realizar las consultas solicitadas
df = pd.read_csv("Datasets/peliculas.csv")
df2 = pd.read_csv("Datasets/peliculas_ml.csv")

#Genero los App para el consumo de la API | Generar HTML

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    '''Ingresas el idioma, retornando la cantidad de peliculas producidas en el mismo'''
    cantidad_peliculas = len(df[df['original_language'] == idioma])
    return {'idioma': str(idioma), 'cantidad': str(cantidad_peliculas)}

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    '''Ingresas la pelicula, retornando la duracion y el año'''
    pelicula_info = df[df['title'] == pelicula]
    duracion = pelicula_info['runtime'].values[0]
    anio = pelicula_info['release_year'].values[0]
    return {'pelicula': pelicula, 'duracion': str(duracion), 'anio': str(anio)}
    
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''  
    franquicia_df = df[df['belongs_to_collection'] == franquicia]
    cantidad_peliculas = franquicia_df.shape[0]
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean()

    return {
        'franquicia': franquicia,
        'cantidad': str(cantidad_peliculas),
        'ganancia_total': str(ganancia_total),
        'ganancia_promedio': str(ganancia_promedio)
    }

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    peliculas_pais_df = df[df['production_countries'].str.contains(pais, na=False)]
    cantidad_peliculas = peliculas_pais_df.shape[0]

    return {
        'pais': pais,
        'cantidad': str(cantidad_peliculas)
    }
    

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    productora_df = df[df['production_companies'].str.contains(productora, na=False)]
    if productora_df.empty:
        return 'El valor solicitado es nulo'
    revenue_total = productora_df['revenue'].sum()
    cantidad_peliculas = productora_df.shape[0]

    return {
        'productora': productora,
        'revenue_total': str(revenue_total),
        'cantidad': str(cantidad_peliculas)
    }

#Modelo de recomendación Machine Learning
#En primer lugar voy a importar las librerias necesarias para comenzar a hacerlo
#Leo el dataframe correspondiente que voy a utilizar para implementarlo luego de aplicar el ETL y el EDA
from sklearn.metrics.pairwise import cosine_similarity
data = pd.read_csv("Datasets/peliculas_ml.csv", low_memory=False)  

#Recorto el Dataframe para poder aplicar el modelo
n=1000 
datos = data.head(n)

#Alimento la variable X con los nombre de las columnas para poder aplicar el modelo
X = datos[['belongs_to_collection', 'genres', 'original_language', "popularity", "production_companies", "release_date", "status", "vote_average", "return"]] 

#Aplico el modelo de Machine Learning de similaridad del coseno
matris = cosine_similarity(X)

#Recomendacion >> Funcion en donde obtengo el indice del titulo segun el parametro luego obtengo los indices de peliculas similares
#Finalmente busco en el dataframe el titulo de las peliculas similares y las retorno para visualizarlas en una lista
@app.get('/recomendacion/{titulo:str}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    top_n=5
    indice_titulo = data[data['title'] == titulo].index[0]  
    resultado_matris = matris[indice_titulo]
    indices = resultado_matris.argsort()[-top_n-1:-1][::-1]  
    recomendacion = data.loc[indices,"title"]  
    recomendacion = recomendacion.values.tolist()
    return {'lista recomendada': str(recomendacion)}