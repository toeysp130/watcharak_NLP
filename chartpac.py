import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from matplotlib import pyplot as plt


f = open("holy_grail.txt","r")
holy_grail = f.read()

lines = holy_grail.split('\n')
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern,'',l) for l in lines]
tokenized_lines = [regexp_tokenize(s,'\w+') for s in lines]

line_num_word = [len(t_line) for t_line in tokenized_lines]
plt.hist(line_num_word)
plt.show()