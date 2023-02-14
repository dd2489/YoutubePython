import os
from pytube import YouTube

# Nombre del archivo que contiene las URL de YouTube
filename = "videos.txt"

folder = "videos"
i = 1
# Crear la carpeta si no existe
if not os.path.exists(folder):
    os.makedirs(folder)

# Leer las URL de YouTube desde el archivo
with open(filename, "r") as file:
    urls = file.readlines()

# Recorrer cada URL y descargar el video si no existe
for url in urls:
    url = url.strip()
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_filename = video.default_filename
    filepath = os.path.join(folder, video_filename)
    if not os.path.exists(filepath):
        video.download(folder)
        print(f"Video descargado: {filepath}")
    else:
        print(f"Video ya existe: {filepath}")
