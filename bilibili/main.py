from bilibili.get_words import getHTML
from bilibili.word_cloud import make_wordcloud


url="https://api.bilibili.com/x/v2/reply?type=1&oid="
#oid=input("input your oid:")
oid = '61602400'
html=url+oid+'&pn='
getHTML('av'+oid, html)
make_wordcloud(oid)