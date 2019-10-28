# -*- coding: utf-8 -*-
import os
from pyltp import Parser
from pyltp import Segmentor
from pyltp import Postagger

LTP_DATA_DIR = '/Users/chenjiarui/PycharmProjects/NLP_exp3/ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

parser = Parser()  # 初始化实例
parser.load(par_model_path)  # 加载模型
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型


text = open("chinese_sen.txt").read()


words_list = list(segmentor.segment(text))  # 分词


postags = postagger.postag(words_list)  # 词性标注


arcs = parser.parse(words_list, postags)

print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

parser.release()  # 释放模型

