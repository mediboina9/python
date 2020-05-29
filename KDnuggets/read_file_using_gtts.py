from gtts import gTTS
import os

file=open('draft.txt','r').read().replace('\n',' ')
language='en'

speeach=gTTS(text=str(file), lang=language, slow=False)

speeach.save('samantha.mp3')
os.system('start samantha.mp3')
