import nltk 
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
for i in range(10) : 
    f = open(f"ch3\wiki\wiki_article_{i}.txt","r")
    article = f.read()
    tokens = word_tokenize(article)
    lower_token = [t.lower() for t in tokens]
    alpha_only = [t for t in lower_token if t.isalpha()]
    no_stop = [t for t in alpha_only if t not in stopwords.words('english')]
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stop]
    articles.append(lemmatized)

dictionary = Dictionary(articles)
computer_id = dictionary.token2id.get("computer")
# print(computer_id)
# print(dictionary.get(computer_id))

corpus = [dictionary.doc2bow(a) for a in articles]
doc = corpus[0]
bow_doc = sorted(doc,key=lambda w : w[1], reverse=True)
for word_id, word_count in bow_doc[:5] : 
    print(dictionary.get(word_id),word_count)

total_word_count = defaultdict(INT)
for word_id,word_count in intertool.chain.from_iterable(corpus) : 
    total_word_count[word_id] += word_count

sorted_word_count = sorted(total_word_count.items(),key = lambda w : w[1], reverse=True)

for word_id, word_count in sorted_word_count[]:
    print(dictionary.get(word_id,word_count))