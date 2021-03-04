#!/usr/bin/env python3

import xlrd
import sys, os
import time
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io


class Word(object):
    def __init__(self, word1, word2, lang1='en', lang2='cs'):
        self.word1 = word1
        self.word2 = word2
        self.lang1 = lang1
        self.lang2 = lang2

    def __str__(self):
        return '{0} - {1}'.format(self.word1, self.word2)

    def sendToGTTS(self):
        gtts1 = gTTS(text=self.word1, lang=self.lang1)
        gtts2 = gTTS(text=self.word2, lang=self.lang2) # slow=False
        return gtts1, gtts2

    def vocalize(self):
        gtts1, gtts2 = self.sendToGTTS()
        b1 = io.BytesIO()
        b2 = io.BytesIO()

        gtts1.write_to_fp(b1)
        gtts2.write_to_fp(b2)

        self.sound1 = AudioSegment.from_file(io.BytesIO(b1.getvalue()), format="mp3")
        self.sound2 = AudioSegment.from_file(io.BytesIO(b2.getvalue()), format="mp3")

    def play(self):
        play(self.sound1)
        play(self.sound2)

    def createFile(self):
        file = pwd + str(self) + '.mp3'
        gtts1, gtts2 = self.sendToGTTS()
        with open(file, 'wb') as fp:
            gtts1.write_to_fp(fp)
        with open(file, 'ab') as fp:
            gtts2.write_to_fp(fp)

###############
pwd = os.getcwd() + '/'
xlloc = pwd + (r'tat_wordlist.xls')
xlbook = xlrd.open_workbook(xlloc)
xlsheet = xlbook.sheet_by_index(0)

wordlist = [Word(str(xlsheet.cell_value(i, 0)), str(xlsheet.cell_value(i, 1))) for i in range(1,xlsheet.nrows)]

for word in wordlist:
    word.vocalize()
    word.createFile()
    word.play()
