from collections import Counter
from nltk.tokenize import word_tokenize

f = open("wiki_article.txt","r")
article = f.read()
tokens = word_tokenize(article)

print(tokens)