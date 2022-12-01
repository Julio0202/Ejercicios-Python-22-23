from pytube import YouTube  
from pytube import Playlist
def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download
def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        cancion.streams.get_audio_only().download("Canciones")
        print("Descargando cancion:", cancion.author)

url = "https://www.youtube.com/watch?v=HKNz0DWQXZw&list=PLVwXkzK42QWrWyeunQ_hi4OM8iUrBWUlq"
descargarLista(url)
