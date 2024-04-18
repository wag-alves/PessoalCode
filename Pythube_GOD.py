#python -m venv venv (criar um ambiente virtual)
#pip install pytube (faz isso no terminal, instala a biblioteca no ambiente virtual)
#venv/scripts/activate (ativa o ambiente virtual)
from pytube import YouTube
from pytube.cli import on_progress

link = str(input(f'Copie o link do vídeo: '))

url = YouTube(link,on_progress_callback=on_progress)

query = url.streams.filter(file_extension='mp4',adaptive=True,only_audio=True)

for item in query:
    print(f'{item}')

option = int(input(f'Digite a Itag da opção desejada: '))

selected = query.get_by_itag(option)
selected.download(r"C:\Users\wag_f\OneDrive\Desktop\PyThube")
print()
