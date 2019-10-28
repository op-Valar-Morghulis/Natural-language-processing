# import nltk
#
# file = open('English.txt')
# text = file.read()
#
# consequence = nltk.word_tokenize(text)
# print(consequence)

import spacy

file = open('English.txt')
text = file.read()

nlp = spacy.load("en_core_web_sm")

test_doc = nlp(text)

for token in test_doc:
    print(token, end="/")


# from stanfordcorenlp import StanfordCoreNLP
#
#
# file = open('English.txt')
# text = file.read()
#
# with StanfordCoreNLP(r'/Users/chenjiarui/Desktop/stanford-corenlp-full-2018-02-27') as nlp:
#     print("/".join(nlp.word_tokenize(text)))


