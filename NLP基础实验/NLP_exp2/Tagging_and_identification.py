import spacy

#加载默认的模型english-core-web
nlp = spacy.load('en')

#加载文本文件来创建
document = open('English.txt').read()

document = nlp(document)

# #词性标注
# for token in document:
#     print(token, token.pos_, end=' / ')

#命名实体识别
for ent in document.ents:
    print(ent, ent.label_, end=' / ')










