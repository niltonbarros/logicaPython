from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Digite o link do vídeo: ")
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
print("Baixando...")
ys.download()
print("Download concluído!")