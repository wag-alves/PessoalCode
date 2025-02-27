import re
import json
import requests
from urllib.parse import parse_qs, unquote

def get_video_url(youtube_url):
    headers = {"User-Agent": "Mozilla/5.0"}

    # 1️⃣ Baixar o HTML da página
    response = requests.get(youtube_url, headers=headers)
    html = response.text

    # 2️⃣ Encontrar o JSON que contém os streams de vídeo
    match = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", html)
    if not match:
        print("Erro: Não foi possível encontrar os dados do vídeo.")
        return None

    # 3️⃣ Carregar o JSON com informações do vídeo
    data = json.loads(match.group(1))
    
    try:
        # 4️⃣ Pegar as URLs de streaming
        streaming_data = data["streamingData"]
        formats = streaming_data["formats"] + streaming_data["adaptiveFormats"]

        # 5️⃣ Pegar a primeira URL disponível
        for fmt in formats:
            if "url" in fmt:
                return fmt["url"]
            
            # Se a URL estiver assinada, precisamos decodificá-la
            if "signatureCipher" in fmt:
                cipher_data = parse_qs(fmt["signatureCipher"])
                return unquote(cipher_data["url"][0])

    except KeyError:
        print("Erro: Formato do JSON mudou e não foi possível encontrar as URLs.")
        return None

    return None

def download_video(video_url, filename="video.mp4"):
    if not video_url:
        print("Erro: URL do vídeo inválida.")
        return

    print(f"Baixando vídeo de: {video_url}")
    headers = {"User-Agent": "Mozilla/5.0"}

    # Fazer o download do vídeo
    response = requests.get(video_url, headers=headers, stream=True)
    
    # Salvar o arquivo
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print("Download concluído!")

# 🔴 Teste com um link do YouTube
youtube_link = "https://www.youtube.com/watch?v=aezstCBHOPQ&list=LL&index=9"
video_direct_url = get_video_url(youtube_link)

if video_direct_url:
    download_video(video_direct_url)
else:
    print("Erro ao obter a URL do vídeo.")
