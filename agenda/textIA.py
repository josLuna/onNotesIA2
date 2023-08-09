"""Analisis de lenguaje natural"""
import spacy
from googleapiclient.discovery import build

nlp = spacy.load('es_core_news_sm')

def analizar_texto(texto):
    doc = nlp(texto)
    
    # Realiza tareas de procesamiento de lenguaje natural según las necesidades
    # Extracción de palabras clave
    palabras_clave = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ']]
    
    return palabras_clave

actividad = "Hacer caldo de pollo con verduras"
palabras_clave = analizar_texto(actividad)
print(palabras_clave)


# Crea un objeto de servicio de la API de YouTube
youtube = build('youtube', 'v3', developerKey='AIzaSyBtXfyvrRbMqcdZBSSCTcb0WySRLEpbiKA')#Clave API

# Define los parámetros de búsqueda para obtener recomendaciones basadas en el término de búsqueda
search_term = palabras_clave

# Realiza la solicitud a la API de YouTube para buscar videos relacionados
response = youtube.search().list(
    part='snippet',
    q=search_term,
    type='video',
    maxResults=4  # Número de videos recomendados que deseas obtener
).execute()

# Extrae los ID de los videos recomendados
video_ids = [item['id']['videoId'] for item in response['items']]

# Genera los enlaces a los videos recomendados
video_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]

# Imprime los enlaces a los videos recomendados
for link in video_links:
    print(link)
