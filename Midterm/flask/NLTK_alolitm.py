from cgi import print_directory
import itertools
from logging.config import dictConfig
from typing import List
import nltk 
from gensim.models.tfidfmodel import TfidfModel
from collections import defaultdict
from gensim.corpora import Dictionary
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

articles = []
def Algolitm(name,key) :
    for i in name : 
        f = open(i,"r")
        article = f.read()
        tokens = word_tokenize(article)
        lower_token = [t.lower() for t in tokens]
        alpha_only = [t for t in lower_token if t.isalpha()]
        no_stop = [t for t in alpha_only if t not in stopwords.words('english')]
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stop]
        articles.append(lemmatized)
    
    global dictionary 
    dictionary = Dictionary(articles)
    computer_id = dictionary.token2id.get(key)
    # print(computer_id)
    # print(dictionary.get(computer_id))
    if(computer_id != None) :
        print(dictionary)
        print('%'*30)
        return "Ok! this keyword found!!"
    else :
        return "Sorry keyword not found"

def BOW() :
    print(dictionary)
    top5 = []
    corpus = [dictionary.doc2bow(a) for a in articles]
    total_word_count = defaultdict(int)
    for word_id,word_count in itertools.chain.from_iterable(corpus) : 
        total_word_count[word_id] += word_count
    sorted_word_count = sorted(total_word_count.items(),key = lambda w : w[1], reverse=True)

    for word_id, word_count in sorted_word_count[:5] : 
        t = dictionary.get(word_id),word_count
        top5.append(t)
    return top5
