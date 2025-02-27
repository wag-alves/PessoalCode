import yt_dlp

video_url = "https://www.youtube.com/watch?v=aezstCBHOPQ&list=LL&index=9"

# Configuração do yt-dlp
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'video.mp4',  # Nome do arquivo de saída
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download concluído!")
