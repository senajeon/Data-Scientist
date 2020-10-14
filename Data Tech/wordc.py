from konlpy.tag import Kkma
from re import match
from collections import Counter
import pytagcloud
import webbrowser

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

def showGraph(wordInfo):
    
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)
    
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

    plt.show()

file = open("test.txt", mode='r', encoding='utf-8')
doc = file.read()
file.close()
print(doc)

kkma = Kkma()

ex_sent = kkma.sentences(doc)

kkma.pos


nouns = []
for sent in ex_sent : 
    for noun in kkma.nouns(sent) :
        # 단어 전처리 : 2음절 이상, 수사 제외
        if len(str(noun)) >= 2 and not(match('^[0-9]', noun)) :
            nouns.append(noun)

print(nouns)

word_count = {}

for noun in nouns :
    word_count[noun] = word_count.get(noun, 0) + 1

counter = Counter(word_count)

top5 = counter.most_common(15)

print(top5)

wordInfo = dict()
for tags, counts in top5:
    if (len(str(tags)) > 1):
        wordInfo[tags] = counts
        # print ("%s : %d" % (tags, counts))
        
showGraph(wordInfo)


word_count_list = pytagcloud.make_tags(top5, maxsize=50)
print(word_count_list)

pytagcloud.create_tag_image(word_count_list,'wordcloud.jpg',size=(900, 600),fontname='Nobile',rectangular=False)

webbrowser.open('wordcloud.jpg')
