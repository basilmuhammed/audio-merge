# -*- coding: utf-8 -*-
from pydub import AudioSegment  # Import this module first
# Load two mp3 audios that need to be merged
input_music_1 = AudioSegment.from_ogg("1.ogg") 
input_music_2 = AudioSegment.from_ogg("2.ogg") 
#Get the loudness (volume) of two audios
input_music_1_db = input_music_1.dBFS
input_music_2_db = input_music_2.dBFS
# Get the duration of two audios in milliseconds
input_music_1_time = len(input_music_1)
input_music_2_time = len(input_music_2)
# Adjust the loudness of the two audios
db = input_music_1_db- input_music_2_db
if db > 0:
    input_music_1 += abs(dbplus)
elif db < 0:
    input_music_2 += abs(dbplus)
# 
output_music = input_music_1 + input_music_2
# Simple input audio after merging
output_music.export("output_music.ogg", format="ogg")# Save path, followed by save format
# Complex input audio after merging
# bitrate:bit rate, album: album name, artist: singer, cover: cover image
# output_music.export("./output_music.mp3", format="mp3", bitrate="192k", tags={"album": "album", "artist": "singer"}, cover="E: / cover.jpg") 
# print(len(output_music), output_music.channels)
# # Combine the duration of the audio, the audio channel, 1 is mono, 2 is stereo
