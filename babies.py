from gtts import gTTS
import os
import pyglet
from time import *
import sys
f = open(os.devnull, 'w')
sys.stdout = f
def say(text):
    tts = gTTS(text=text, lang='en-uk')
    filename = '/tmp/temp.mp3'
    tts.save(filename)
    start2=time()
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    end2=time()
    sleep(music.duration) #prevent from killing
    os.remove(filename) #remove temperory file
def babies(doing,error,times,said):
    for x in range(0,times):
        saymeup=str(times-x)+"little babies"+doing+error+"Mommy called the daddy and the daddy sed"+said
        if(x!=times-1):
            say(saymeup)
try:
    optional=sys.argv[4]
except IndexError:
    optional= " no more babies"+sys.argv[1]
babies(sys.argv[1],sys.argv[2],int(sys.argv[3]),optional)
