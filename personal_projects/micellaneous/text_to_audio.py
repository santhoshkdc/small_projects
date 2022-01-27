from gtts import gTTS
import os

mytext = "I did this code by myself"
language = 'en'
myobj = gTTS(text=mytext,lang=language,slow=False)
myobj.save("save.mp3")
os.system("save.mp3")
