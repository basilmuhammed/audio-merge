#!usr/local/bin/python
import glob
import sys
import os

from pydub import AudioSegment
dirpath = "news/"
headingsNewsDir = dirpath+"2019-03-01/"
includeDir = dirpath+"/include/"
generatedFile = "combined_news_file.ogg"

filenames = glob.glob(headingsNewsDir+'*.ogg')
welcome  = AudioSegment.from_ogg(includeDir + "1.ogg")
thankyou = AudioSegment.from_ogg(includeDir + "2.ogg")
# beep     = AudioSegment.from_wav(includeDir + "beep.wav")

filenameswithbeep = [welcome, beep]
combined = AudioSegment.empty()
for filename in filenames:
	audiofilename = AudioSegment.from_ogg(filename)
	filenameswithbeep.extend([audiofilename, beep])

filenameswithbeep.extend([thankyou])

for fname in filenameswithbeep:
    combined += fname

combined.export(headingsNewsDir + generatedFile, format="ogg")

#for fname in filenames:
	#os.remove(fname)