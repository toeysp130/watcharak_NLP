from cgi import print_arguments
from lib2to3.pgen2.tokenize import tokenize
import math
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re
#print(word_tokenize("Hi there!"))
f = open("scene_one.txt","r")
scene_one = f.read()
#print(scene_one)

sentences = sent_tokenize(scene_one)
#print('sentences = ', sentences)

tokenized_sent = word_tokenize(sentences[3])
#print('tokenized_sent = ',tokenized_sent)

unique_token = set(word_tokenize(scene_one))
#print(unique_token)
#print(len(unique_token))

match = re.search("coconuts",scene_one)
#print(match)

pattern1 = r"\[.*]"
#print(re.search(pattern1,scene_one))

pattern2 = r"['A-z\s\d']+:"
#print(re.match(pattern2,sentences[3]))

match_digits_and_words = ('(d+|\w+)')
#print(re.findall(match_digits_and_words,'He has 11 cats'))

my_str = 'match lowercase spaces nums like 12, but no commas'
match_str = ('[a-z0-9 ,]+')
#print(re.match(match_str,my_str))

from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
match_string = r"(#\d\w+\?!)"
#print(re.match(match_string,my_string))

tweets = ['This is the #nlp exercise! #python', '#NLP is superfun! <3 #learning', 'Thanks @fitmkmutnb :) #nlp #python']
pattern1 = r"#\w+"
hashtags = regexp_tokenize(tweets[0],pattern1)
#print(hashtags)

pattern2 = r"([@]\w+)"
mentions_hashtags = regexp_tokenize(tweets[-1],pattern2)
#print(mentions_hashtags)

tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)
