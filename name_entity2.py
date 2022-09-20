from cProfile import label
from collections import defaultdict
from lib2to3.pgen2.tokenize import tokenize
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize 
from matplotlib import pyplot as plt

# nltk.download('words')
# nltk.download('maxent_ne_chunker')
# nltk.download('averaged_perceptron_tagger')

f = open(".\ch4\\tim_cook.txt","r")
article = f.read()

sentences = nltk.sent_tokenize(article)    #แตกเป็นคำ
token_sentence = [nltk.word_tokenize(sent) for sent in sentences]

pos_sentences = [nltk.pos_tag(sent) for sent in token_sentence]

#chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)  #ใช้คู่กับบรรทัดที่ 24-27
chunked_sentences = nltk.ne_chunk_sents(pos_sentences)


# for sent in chunked_sentences :
#     for chunk in sent :
#         if hasattr(chunk,"label") and chunk.label() == "NE" :
#             print(chunk)
ner_categories = defaultdict(int) #กำหนดค่า pie chart


for sent in chunked_sentences :
    for chunk in sent :
        if hasattr(chunk,"label") :
            ner_categories[chunk.label()] += 1

labels = list(ner_categories.keys())
values = [ner_categories.get(v) for v in labels]

#สร้าง piechart
plt.pie(values,labels=labels,autopct='%1.1f%%',startangle=140)

plt.show()
