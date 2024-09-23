import io
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))
file1 = open("text.txt")


line = file1.read()
words = line.split()
for r in words:
	if not r in stop_words:
		appendFile = open('filteredtext.txt','a')
		appendFile.write(" "+r)
		appendFile.close()


#INPUT ->
# The author illustrates the conflict between marrying for money, which was the typical idea at the time, and marrying for love.


#OUTPUT ->
# The author illustrates conflict marrying money, typical idea 
# time, marrying love. 
