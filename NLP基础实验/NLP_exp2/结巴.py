import jieba.posseg as pseg

file = open('Chinese.txt')

sentence = file.read()

# seg_list = jieba.cut(sentence, cut_all=False)

words = pseg.cut(sentence)

for word, flag in words:
    print(word, flag,end="/")


file.close()

