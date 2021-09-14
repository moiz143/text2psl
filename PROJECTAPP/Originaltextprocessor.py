from string import punctuation

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer


def preprocess_text(text):
  print('preprocess text function executed')

  # CONTRACTION



  #convert numbers into text



  # TOKENIZE THE SENTENCE
  text = word_tokenize(text)


  # REMOVE ALL TOKENS THAT ARE NOT ALPHABETIC
  text = [word for word in text if word.isalpha()]


  # GET ALL THE STOP WORDS FOR ENGLISH
  #new_stopwords = set(stopwords.words('english'))
  new_stopwords = set(stopwords.words('english')) - {'so','too','there','if','open','close','i', 'me', 'my', 'myself', 'we', 'our', 'you', 'your', 'he', 'him', 'his', 'she', 'her', 'what', 'which', 'who', 'about', 'before', 'after', 'above', 'below', 'again', 'here', 'when', 'where', 'why', 'how', 'all', 'no', 'nor', 'not', 'same', 's', 't', 'now', 'this', 'that'}


  #  REMOVE THE STOP WORDS
  text = [word for word in text if not word in new_stopwords]

  #For LEMMATIZER
  #lemmatizer = WordNetLemmatizer()
  #text = [lemmatizer.lemmatize(word) for word in text]


  # FOR STEMMING
  #porter = PorterStemmer()
 # text = [porter.stem(word) for word in text]


  return text