from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from os import path
import jieba

def make_wordcloud(oid):
    cur_path = path.dirname(__file__)  # 当前路径
    file = 'av' + oid + '_replies.txt'
    # print('path: ',path.join(cur_path, './replies', file), encoding='utf-8'))
    text = open(path.join(cur_path, './replies', file), encoding='utf-8').read()  # 读取的文本
    # jieba.add_word(word1)
    # jieba.add_word(word2)    #添加结巴分辨不了的词汇
    jbText = ' '.join(jieba.cut(text))
    imgMask = np.array(Image.open(path.join(cur_path, './images', 'msk.png')))  # 读入背景图片
    wc = WordCloud(
        background_color='white',
        max_words=500,
        font_path='msyh.ttc',  # 默认不支持中文
        mask=imgMask,  # 设置背景图片
        random_state=30  # 生成多少种配色方案
    ).generate(jbText)
    ImageColorGenerator(imgMask)  # 根据图片生成词云颜色
    # plt.imshow(wc)
    # plt.axis('off')
    # plt.show()
    wc.to_file(path.join(cur_path, './images/av' + oid + '.png'))
    print('成功保存词云图片！')

if __name__ == '__main__':
    oid = '73617352'
    make_wordcloud(oid)
