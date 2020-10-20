# -*- coding: utf-8 -*-
import os
import glob
from pydub import AudioSegment  # Import this module first



# Load two mp3 audios that need to be merged
input_music_1 = AudioSegment.from_ogg("audio/1.ogg") 
input_music_2 = AudioSegment.from_ogg("audio/2.ogg") 

#Get the loudness (volume) of two audios
input_music_1_db = input_music_1.dBFS
input_music_2_db = input_music_2.dBFS

# Get the duration of two audios in milliseconds
input_music_1_time = len(input_music_1)
input_music_2_time = len(input_music_2)
 
output_music = input_music_1 + input_music_2
# Simple input audio after merging
output_music.export("output_music.ogg", format="ogg")# Save path, followed by save format

