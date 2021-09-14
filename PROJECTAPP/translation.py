from googletrans import Translator


translator = Translator()
trans = translator.translate('میرا نام ہے',  dest='en')
text = trans.text

print(text)