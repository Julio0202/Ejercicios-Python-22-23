from pytube import YouTube  
def descargaCancion(url:str):
    youtube = Youtube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download
descargaCancion("")
