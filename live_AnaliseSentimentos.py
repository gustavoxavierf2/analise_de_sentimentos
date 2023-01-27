import nltk
nltk.dowload()
'''
nltk.download("movie_reviews")
nltk.download("punkt")

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from googletrans import Translator

texto = str(input("digite: "))
traduzir = Translator()
a = traduzir.translate(texto, dest="en").text
print(a)
a = TextBlob(traduzir.translate(texto, dest="en"), analyzer=NaiveBayesAnalyzer())
print(a.sentiment)'''