# coding=utf-8
# 功能: 提取关键字，生成词云
# 创建者：俺

import jieba.posseg as pseg
import wordcloud
import tkinter
from PIL import Image, ImageTk

file_name = input('请输入需要转换的文件名:')
file = open(f'{file_name}', encoding='utf-8')
str = file.read()
file.close()
wlist = pseg.lcut(str)
wtimes = {}
cstr = []
sw = []

for a in wlist:
    if a.flag == 'nr':
        wtimes[a.word] = wtimes.get(a.word, 0) + 1
        cstr.append(a.word)
    else:
        sw.append(a.word)
wlist = list(wtimes.keys())
wlist.sort(key=lambda x: wtimes[x], reverse=True)
for a in wlist[:10]:
    print(a, wtimes[a], sep='\t')
text = ' '.join(cstr)

font_name = input('请输入字体文件名:')
img_width =  int(input('请输入转换的图片高度:'))
img_height =  int(input('请输入转换的图片宽度:'))
cloud = wordcloud.WordCloud(font_path=font_name, background_color='white'
                            , stopwords=sw, collocations=False
                            , width=img_width, height=img_height).generate(text)

file = cloud.to_file(f'{file_name}.jpg')
root = tkinter.Tk()
img = Image.open(f'{file_name}.jpg')
pic = ImageTk.PhotoImage(img)
imgLabel = tkinter.Label(root, image=pic)
imgLabel.pack()
root.mainloop()