import re

#word_regex = '\w+'

#print(re.match(word_regex, 'hi there!'))

#print(re.split('\s+','Split on spaces.'))

#my_string  = "Let's write RegEx!"
#print(re.findall(r"\w+",my_string))

my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"
#sentence_endings = r"[\!+?+.]"
#capitalized_word = r"[A-Z]\w+"
#space = r"\s+"
digits = r"\d+"
#print(re.split(sentence_endings,my_string))

#print(re.findall(capitalized_word,my_string))
#resule -> ['Let', 'RegEx', 'Won', 'Can', 'Or']

#print(re.split(space,my_string))
#resule -> ["Let's", 'write', 'RegEx!', "Won't", 'that', 'be', 'fun?', 'I', 'sure', 'think', 'so.', 'Can', 'you', 'find', '4', 'sentences?', 'Or', 'perhaps,', 'all', '19', 'words?']#print(re.split(space,my_string))

print(re.findall(digits,my_string))
#resule -> ['4', '19']