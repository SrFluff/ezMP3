from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

ezversion = "1.1.0"

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
