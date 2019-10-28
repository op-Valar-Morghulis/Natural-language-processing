from snownlp import SnowNLP

document = open('Chinese.txt').read()

s = SnowNLP(document)

a = s.tags


print(list(a))



