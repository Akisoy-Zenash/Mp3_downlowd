from pytube import YouTube
from pytube import Playlist
import os

#la playlist que je veut 
plist = Playlist("https://youtube.com/playlist?list=PLlKPfDQ7VPGG7FTto-Igt03DO2MZOTTu3")
#le dossier ou je vais la mettre
destination = "C:/Users/akiso/Downloads/py_musique"

#recup url de chaque vid et downlowd
for url in plist:
    #affiche url
    print(url)

    #prendre que l'audio
    vid = YouTube(url)
    audio = vid.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path=destination)

    #ctrl+c ctrl+v jsp trop se que ca fait de se que je voit ca convertie .mp3 et save dans le bon dossier
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  
    #afficher si tout va bien
    print(vid.title + " has been successfully downloaded.")

#afficher fin
print("All Successfully downloaded")

