import nltk

f = open("test_LM.txt", "r").read()

text = 'PythonTip.com is a very good website. We can learn a lot from it .'
#将文本拆分成句子列表

f.split("__eou__ ", 2)
sens = nltk.sent_tokenize(f)
words = []
for sent in sens:
    words.append(nltk.word_tokenize(sent))

from nltk import WordPunctTokenizer
words = WordPunctTokenizer().tokenize(sens)

print(words)



# print(sentences)




# bigrams = ngrams(text6, 2)
# bigramDist = FreqDist(bigrams)
# print(bigramDist.most_common(10))
# f.close()
# print(os.path.abspath('.'))