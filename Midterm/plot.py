from matplotlib import pyplot as plt
from pkg_resources import working_set
from nltk.tokenize import word_tokenize
plt.hist([1,5,5,7,7,7,9])
#plt.show()

words = word_tokenize("This is a pretty cool tool!")
word_lengths = [len(w) for w in words]
plt.hist(word_lengths)
plt.show()