import gtts
import os
text="aCCORDING TI WIKIPEDIA Siva IS BIG CODER AND HE CREATED ONE TEXT SPEEACH PROGRAM WITH ONLINE WEBSITE KDNUGGETS"
language="en"
speech=gtts.gTTS(text=text, lang=language, slow=False)
speech.save("text1.mp3")
os.system("start text1.mp3")
