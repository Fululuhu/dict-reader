#!/usr/bin/env python3

import xlrd
import sys, os
import time
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io


def translate(english, czech):
    sound_english = gTTS(text=english, lang='en')
    sound_czech = gTTS(text=czech, lang='cs') # slow=False
    return sound_english, sound_czech

def createFile(english, czech, file):
    with open(file, 'wb') as fp:
        english.write_to_fp(fp)
    with open(file, 'ab') as fp:
        czech.write_to_fp(fp)

def say(english, czech):
    fp_english = io.BytesIO()
    english.write_to_fp(fp_english)
    playMp3(fp_english)
    time.sleep(0.5)
    fp_czech = io.BytesIO()
    czech.write_to_fp(fp_czech)
    playMp3(fp_czech)

    time.sleep(1)

def playMp3(sound):
    
    song = AudioSegment.from_file(io.BytesIO(sound.getvalue()), format="mp3")
    play(song)

###############

pwd = os.getcwd() + '/'
xlloc = pwd + (r'tat_wordlist.xls')
xlbook = xlrd.open_workbook(xlloc)
xlsheet = xlbook.sheet_by_index(0)
wordlist = {str(xlsheet.cell_value(i, 0)):str(xlsheet.cell_value(i, 1)) for i in range(1,xlsheet.nrows)}

for word_english in wordlist.keys():
    word_czech = wordlist[word_english]
    file = pwd + '{0} - {1}.mp3'.format(word_english, word_czech)
    english, czech = translate(word_english, word_czech)
    print('{0} - {1}'.format(word_english, word_czech))
    

    createFile(english, czech, file)
    say(english, czech)
