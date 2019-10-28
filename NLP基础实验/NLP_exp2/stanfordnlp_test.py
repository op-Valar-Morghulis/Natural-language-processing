from stanfordcorenlp import StanfordCoreNLP


nlp = StanfordCoreNLP(r'/Users/chenjiarui/Desktop/stanford-corenlp-full-2018-02-27', lang="zh")

document = open('English.txt').read()

print('Tokenize:', nlp.word_tokenize(document))

# print("-------------------------------------------")
# print('Part of Speech:', nlp.pos_tag(document))


print("-------------------------------------------")

print('Named Entities:', nlp.ner(document))

nlp.close()
