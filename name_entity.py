from lib2to3.pgen2.tokenize import tokenize
import nltk
nltk.download('words')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
sentence = 'On the 15th of September, Tim Cook announced that Apple wants to acquire ABC Group from New York for 1 billion dollars.'
tokenize_sent = nltk.word_tokenize(sentence)
tagged_sent = nltk.pos_tag(tokenize_sent)

print(tagged_sent)
print(nltk.ne_chunk(tagged_sent))