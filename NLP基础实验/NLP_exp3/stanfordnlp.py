from stanfordcorenlp import StanfordCoreNLP

#使用stanfordcorenlp进行句法分析和依存句法分析

nlp = StanfordCoreNLP(r'/Users/chenjiarui/Desktop/stanford-corenlp-full-2018-02-27', lang="zh")

sentence = open("chinese_sen.txt").read()

print("Constituency Parsing:", nlp.parse(sentence))

print("Dependency Parsing", nlp.dependency_parse(sentence))

nlp.close()
