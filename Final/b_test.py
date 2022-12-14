from ast import Str
import nltk
import itertools
import os
from collections import defaultdict
from gensim.corpora import Dictionary
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
articles = []
for i in range(0,10):
    f = open(f"./wiki/wiki_article_{i}.txt", "r") #ใช้ใน mac
    #C:\Users\watcharak2059\Desktop    #ใช้กับห้อง Lab
    #อ่านไฟล์บนแม็กกับวินโดว์ใช้ใช้สแลช Path ต่างกัน
    article = f.read()
    tokens = word_tokenize(article)
    lower_token = [t.lower() for t in tokens]
    alpha_only = [t for t in lower_token if t.isalpha()]
    no_stop = [t for t in alpha_only if t not in stopwords.words('english')]
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stop]
    articles.append(lemmatized)

dictionary = Dictionary(articles)
# computer_id = dictionary.token2id.get("computer")
# print(computer_id)
# print(dictionary.get(computer_id))

corpus = [dictionary.doc2bow(a) for a in articles]
# doc = corpus[0]
# bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)
# for word_id, word_count in bow_doc[:5]:
#     print(dictionary.get(word_id), word_count)

total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count

sorted_word_count = sorted(total_word_count.items(),
                           key=lambda w: w[1], reverse=True)

for word_id, word_count in sorted_word_count[:1]:
    print("Hot Hit : ",dictionary.get(word_id),word_count)

print("Don't dupplicate : " ,len(sorted_word_count))
