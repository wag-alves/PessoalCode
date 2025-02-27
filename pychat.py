import re
import json
import requests

video_url = "https://www.youtube.com/watch?v=aezstCBHOPQ&list=LL&index=9"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(video_url, headers=headers)
html = response.text

match = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", html)
if match:
    data = json.loads(match.group(1))
    streaming_data = data["streamingData"]["formats"]
    video_url = streaming_data[0]["url"]
    print("URL do vídeo:", video_url)

video_data = requests.get(video_url, headers=headers)
with open("video.mp4", "wb") as f:
    f.write(video_data.content)
