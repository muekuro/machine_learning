# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

appid = 'dj0zaiZpPW9IQ29tc2tSSW5jdiZzPWNvbnN1bWVyc2VjcmV0Jng9Mjc-'
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse";

# Yahoo!形態素解析の結果をリストで返す
def split(sentence, appid=appid, results="ma"):
  sentence = sentence.encode("utf-8")
  params = urllib.urlencode({'appid':appid, 'results':results, 'filter':filter,'sentence':sentence})
  results = urllib2.urlopen(pageurl, params)
  soup = BeautifulSoup(results.read(), "html.parser")
  
#   for w in soup.ma_result.word_list:
#       print(w)
  return [w.surface.string for w in soup.ma_result.word_list]

# split('私は人間です'.decode('utf-8'))