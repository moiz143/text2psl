from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import glob

stopwords = stopwords.words('english')
stopwords.append('%')  # Adding more symbols to stop words mostly founded un-attractive
stopwords.append('.')
stopwords.append(',')
stopwords.append('(')
stopwords.append(')')
stopwords.append('{')
stopwords.append('}')
stopwords.append(':')
stopwords.append('\\')
stopwords.append('^')
stopwords.append('_')
stopwords.append('$')
stopwords.append('@')
stopwords.append('e.g')
stopwords.append('The')
stopwords.append('We')
stopwords.append('Our')
stopwords.append('To')
stopwords.append(',')
stopwords.append('As')
stopwords.append(';')
stopwords.append('+')
stopwords.append('1')
stopwords.append('2')
stopwords.append('3')
stopwords.append('4')
stopwords.append('5')
stopwords.append('6')
stopwords.append('7')
stopwords.append('8')
stopwords.append('9')
stopwords.append('0')
stopwords.append('In')
stopwords.append('|')
stopwords.append('||')
stopwords.append('A')
stopwords.append('This')
stopwords.append('^')

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

path =r'C:\Users\muham\Documents\MPhill (CS) NTU\3rd Semester\Data Scrap\shahzad\untitled5\abstract scraping\Data'
filenames = glob.glob(path + "/*.csv") #Files in directory
for i in filenames:
   # print(i[106:])
    a= i[106:]     #Reading file name from folder like (data mining.csv) 106 is the path length i only need files name

    #filepath =r'C:\Users\muham\Documents\MPhill (CS) NTU\3rd Semester\Data Scrap\shahzad\untitled5\abstract scraping\Data\\'+a
    filepath = path +'\\' + a
    f = open("P-" + a, "w")  # File creating for stroing data after preprosessing
    f.write(a + "\n")
    fp = open(filepath, 'r') #Reading file from directery
    line = fp.readline() #
    a =1
    while line:
       a = a+1
       line = fp.readline()

      # stop_words = set(stopwords.words('english'))
       word_tokens= word_tokenize(line.strip())  #removing extra spaces from file

       filtered_sentence = [w for w in word_tokens if not w in stopwords] #removing stop words from tokenize file

      # filtered_sentence = []

       for w in word_tokens:
           if w not in stopwords:
               filtered_sentence.append(w)           #filtered sentences after removing stop words

      # print(word_tokens)
      # print(a+ "for this file we are doing stemming and removing stop words  ")
       print(filtered_sentence)
       strappend = " "
       for x in filtered_sentence:    # stemming from tokening and  and after stopword removel
           #print(ps.stem(x))

           ver = lemmatizer.lemmatize(x)
           y = ps.stem(ver)
           comm = y.replace(',', '')
           #print(comm)
           strappend += " " + comm  #each string word appended to form a complete sentence
       print(strappend)

       f.write(strappend + "\n")
       if (a==100):
           break
    f.close()
    fp.close()


