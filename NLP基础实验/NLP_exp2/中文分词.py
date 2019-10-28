
from stanfordcorenlp import StanfordCoreNLP


file = open('Chinese.txt')
text = file.read()

with StanfordCoreNLP(r'/Users/chenjiarui/Desktop/stanford-corenlp-full-2018-02-27', lang='zh') as nlp:
    print("/".join(nlp.word_tokenize(text)))

# ------------------------------------------------

# import jieba

# #jieba全模式
# seg_list = jieba.cut(user_dict, cut_all=True)

# #jieba精确模式
# seg_list = jieba.cut(user_dict, cut_all=False)

# #jiaba搜索引擎模式
# seg_list = jieba.cut_for_search(user_dict)

# #jieba的自定义字典模式
# jieba.load_userdict("userdict.txt")
# seg_list = jieba.cut(text)
# print("自定义字典："+"/".join())


# print("Full Mode:"+"/".join(seg_list))

# print("Default Mode："+"/".join(seg_list))

# print("Search Engine Mode："+"/".join(seg_list))

# from snownlp import SnowNLP

# #snownlp
# s = SnowNLP(user_dict)

# print("snowNLP Mode:"+"/".join(s.words))

# import thulac

# #thulac 分词
# thu1 = thulac.thulac(seg_only=True)

# text = thu1.cut(user_dict, text=True)

# print("THULAC:"+"/".join(text))

# import  pynlpir
# pynlpir.open()
#
# #读入中文文本
# file = open('Chinese.txt')
# text = file.read()
#
# segments = pynlpir.segment(text,  pos_english=False)
#
# for segment in segments:
#     print(segment[0], end="/")
#
# pynlpir.close()