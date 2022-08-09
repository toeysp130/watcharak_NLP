from collections import Counter
from nltk.tokenize import word_tokenize

f = open("wiki_article.txt","r")
article = f.read()
tokens = word_tokenize(article)
lower_tokens = [t.lower() for t in tokens]

bow_simple = Counter(lower_tokens)
print(bow_simple.most_common(10))