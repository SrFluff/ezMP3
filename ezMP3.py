from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os

ezversion = "1.2.0"

def version():
    return ezversion

def super(path, tag):
    return EasyID3(path)[tag][0]

def getTitle(path):
    return super(path,"title")

def getAuthor(path):
    return super(path,"artist")

def getAlbum(path):
    return super(path,"album")

def getYear(path):
    return super(path,"date")

def getLength(path):
    return MP3(path).info.length

def getCover(path):
    os.system(f"ffmpeg -hide_banner -loglevel quiet -y -i '{path}' -an -c:v copy '/tmp/ezmp3_cover.png'")
    if os.path.exists("/tmp/ezmp3_cover.png"):
        f = open("/tmp/ezmp3_cover.png","rb")
        rType = f.read()
        f.close()
        os.remove("/tmp/ezmp3_cover.png")
    else:
        rType = -1
    return rType
