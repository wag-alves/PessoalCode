from pytube import YouTube
from pytube.cli import on_progress

link = str(input(f'Copie o link do vídeo: '))

url = YouTube(link,on_progress_callback=on_progress)

query = url.streams.filter(progressive=True)


for item in query:
    print(item)

option = int(input(f'Digite a Itag da opção desejada: '))

selected = query.get_by_itag(option)
selected.download(r"C:\Users\wag_f\OneDrive\Desktop\PyThube")
print()

'''
https://www.youtube.com/watch?v=41p_AqKVeHw&list=LL&index=411
'''