from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize
german_text = "Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕"

all_words = word_tokenize(german_text)
#print(all_words)

capital_words = r"[A-ZÜ]\w+" #pattern to pick word fist upper
#print(regexp_tokenize(german_text,capital_words))

emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(emoji)