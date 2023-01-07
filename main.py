from pytube import YouTube
from pytube import Playlist
import os

plist = Playlist("https://youtube.com/playlist?list=PLlKPfDQ7VPGG7FTto-Igt03DO2MZOTTu3")
destination = "C:/Users/akiso/Downloads/py_musique"


for url in plist:
    print(url)
    vid = YouTube(url)
    audio = vid.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  

    print(vid.title + " has been successfully downloaded.")

print("All Successfully downloaded")
