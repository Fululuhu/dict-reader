import pygame as pg

def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)


# pick a MP3 music file you have in the working folder
# otherwise give the full file path
# (try other sound file formats too)
music_file = "/home/fululuhu/Projects/Tatulda/28 Princezna holubička.mp3"

# optional volume 0 to 1.0
volume = 0.8
link = 'https://translate.google.com/translate_tts?ie=UTF-8&q=hello&tl=en&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=5&tk=316070.156329'
play_music(link, volume)
