# Speech-to-text for Qur'an verses !

Hello, My name is amir and am new in NLP.
My first task as an intern in this field, was processing Qur'an verses to spill it with the highest accuracy.
After 2 weeks of searching, I found the whisper model from hugging face(huggingface.co).

my task was split a verse from Qur'an into 30 seconds and then, process each piece to text.
I hope it helps to you for starting speech processing!
## importing libraries:
you need to install this libraries:
pip install whisper      # note: this library isn't exist for anaconda so don't try: conda install whisper
pip install glob
pip install pydub
pip install sys
pip install os

after that, in which load_model from whisper library, depending on the model you choose, you need to download it.
we have five models frmo this site:
base: 74 Mb
small: 244 Mb
medium: 769 Mb
large: 1550 Mb
large-v2: 1550 Mb

personly, I used _medium_ model from whisper library and Al-Kursi verse for test.

this is a python code and feel free to ues or improve it! 
I'm eagerly wating for your comments
