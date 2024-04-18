import requests

link = requests.get( 'https://www.youtube.com/watch?v=u7f3oD-xsfo', stream=True)

x = link

with open('filename.mp4', 'wb') as fd:
    for chunk in x.raw.iter_content():
        fd.write(chunk)

print(x.raw)
print(x.raw)