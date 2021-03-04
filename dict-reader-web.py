#!/usr/bin/env python3

import xlrd
import os
import time
from gtts import gTTS
import vlc



def create(english, czech, file):
    with open(file, 'wb') as fp:
        english.write_to_fp(fp)
    with open(file, 'ab') as fp:
        czech.write_to_fp(fp)

def say(english, czech, file):
    fp_english = BytesIO()
    english.write_to_fp(fp_english)
    fp_czech = BytesIO()
    czech.write_to_fp(fp_czech)
    fp = [fp_english, fp_czech]
    print(english.get_urls())
	
    

	
    for sound in fp:
	    #print(io.open(sound))
	    player = vlc.MediaPlayer('https://translate.google.com/translate_tts?ie=UTF-8&q=hello&tl=en&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=5&tk=316070.156329')
	    player.play()
	    time.sleep(2)
	    player.stop()


pwd = os.getcwd() + '/'
xlloc = pwd + (r'tat_wordlist.xls')
xlbook = xlrd.open_workbook(xlloc)
xlsheet = xlbook.sheet_by_index(0)
wordlist = {str(xlsheet.cell_value(i, 0)):str(xlsheet.cell_value(i, 1)) for i in range(1,xlsheet.nrows)}

for word_english in wordlist.keys():
    word_czech = wordlist[word_english]
    #file = pwd + '{0} - {1}.mp3'.format(word_english, word_czech)

    print('{0} - {1}'.format(word_english, word_czech))

    link_en = 'https://translate.google.com/translate_tts?ie=UTF-8&q='+ word_english +'&tl=en&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=5&tk=316070.156329'
    player = vlc.MediaPlayer(link_en)
    player.play()
    time.sleep(2)
    player.stop()
    link_cs = 'https://translate.google.com/translate_tts?ie=UTF-8&q='+ word_czech +'&tl=cs&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=5&tk=316070.156329'
    player = vlc.MediaPlayer(link_cs)
    player.play()
    time.sleep(2)
    player.stop()
    
    
