import jieba
import jieba.analyse
import jieba.posseg as pseg
import pynlpir
import ctypes
from os import path
d = path.dirname(__file__)
print(d)
# pynlpir.open()
# s = 'NLPIR分词系统前身为2000年发布的ICTCLAS词法分析系统，从2009年开始，为了和以前工作进行大的区隔，并推广NLPIR自然语言处理与信息检索共享平台，调整命名为NLPIR分词系统。'  # 实验文本
#
# print(pynlpir.segment(s))  # 默认打开分词和词性标注功能
# pynlpir.close()
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# # print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# # keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
# #
# # # print(type(keywords))
# # # <class 'list'>
# #
# # for item in keywords:
# #     print(item[0],item[1])
# #
# #
# #
# # words = pseg.cut("我爱北京天安门")
# # # words类别为：generator
# #
# # for word, flag in words:
# #     print('%s %s' % (word, flag))

