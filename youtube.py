# --------------------------------------------------------------------------------
# Documentação:
#               https://pypi.org/project/pytube/
#
# Atualizando o PIP:
#               python.exe -m pip install --upgrade pip
#
# Instalando a bibliotecao PYTUBE:
#               python.exe -m pip install pytube
# --------------------------------------------------------------------------------

import os, sys
from pytube import YouTube

# Definindo o diretório de salvamento
diretorio = os.path.dirname(os.path.realpath(__file__))

# Solicitando a URL do vídeo
url_video = input('\nInforme a URL do vídeo: ')

try:
    # Criando o objeto 
    yt = YouTube(url_video)
except:
    print('\nERRO..: ', sys.exc_info()[0])
    baixado = False
else:
    # Lista todos os formatos disponíveis
    print('\nLista de Vídeos Disponíveis:')
    videos = yt.streams.all()
    # Indexa os formatos em uma lista
    lista_videos = list(enumerate(videos))
    # Exibe os formatos disponíveis
    for video in lista_videos: print(video)
    # Solicita qual o formato a ser baixado
    opcao_download = int(input('\nInforme a Opção para baixar o formato desejado: ')) 
    try:
        # Efetua o download do vídeo
        video_download = videos[opcao_download]
        video_download.download()
        baixado = True
    except:
        print('\nERRO..: ', sys.exc_info()[0])
        baixado = False
finally:
    if baixado: 
        print('\nVídeo Baixado com Sucesso...\n')
    else:
        print('\nProblema no Download do Vídeo...\n')