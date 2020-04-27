from gtts import gTTS
import os

mText = "hahahahah cyka blyat"

language = 'ru'

output = gTTS(text = mText, lang = language, slow = True)

output.save("output.mp3")

os.system("start output.mp3")