from typing import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
f = open("wiki_article.txt","r")
article = f.read()
tokens = word_tokenize(article)
lower_tokens = [t.lower() for t in tokens]
from nltk.stem import WordNetLemmatizer
alpha_only = [t for t in lower_tokens if t.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('english')] 
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

bow = Counter(lemmatized)
print(bow.most_common(10))