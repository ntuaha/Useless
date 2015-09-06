#encoding=utf-8

import datetime
import psycopg2
import sys
sys.path.append('/home/aha/Other_Project/jieba/')
reload(sys)
sys.setdefaultencoding('utf8')

import jieba
import jieba.analyse
import json
from StringIO import StringIO
import re
import jieba.posseg as pseg

with open("/home/aha/Project/Useless/data/20150821.txt","r") as f:
  lines = f.readlines()
  total_cnt = len(lines)
  i=0
  for i in xrange(0,total_cnt,3):
    line = lines[i]
    io = StringIO(line)
    data = json.load(io)
    data["title"] = lines[i+1]
    data["content"] = lines[i+2]
    sentenses = re.split(unicode("[(\\r)|(\\n)|\s|。|！|？|「|」|...|?|!|,|，]"),data["content"].decode('utf-8'))
    k = False
    with open("/home/aha/Project/Useless/sentense.log","a+") as f2:
      for s in sentenses:
        #if "年約" in s or "歲" in s or "年僅" in s:
        if "歲" in s:
          ss = re.match(unicode("(\d+)歲(.+)"),s)
          age = ss.groups(0)
          i = i+1
          words = pseg.cut(ss.group(1))
          for w in words:
            if and "n" in w.flag and len(w.flag)<=2:
              noun = w.word
              find_n  = False

          f2.write("%d:[%d - %s]"%(i,age,noun))
          for w in words:
            f2.write("%s[%s]|"%(w.word,w.flag))
          f2.write("\n")
          break
    break


s = '但現在全球最老男人瑞還是由112歲的日本人奪下'
words = pseg.cut(s)
find_n = False
find_m = True


with open("/home/aha/Project/Useless/sentense.log","r") as f:
  for line in f:
    if "歲" in line:
      print line
      info = line.split(":")
      words = info[1].split("|")
      for w in words:
        g = re.match("(\w+)\[([a-z]+)\]",w)
        w1 = g.groups(0)
        w2 = g.groups(1)
      break









seg_list = jieba.cut(data["content"])  # 默认是精确模式
print("|".join(seg_list))


ks = re.split('[\r\n,]', '015年08月21日 23:25<a href=\"\/realtimenews\/16\">中時電子報<\/a> <a href=\"\/reporter\/1347\">吳品瑤<\/a> \n\r\n\n女星宋紀妍2013年與大她17歲的新東陽少東麥升陽相戀，交往2個月即決定閃婚，老公對嫩妻疼愛有加，結婚兩年的他們，終於在今年宣布有了「肉鬆公主」，本月14日宋紀妍產下愛女「麥寶」，不僅為了寶貝挨刀剖腹，孩子出生後更是一場硬仗')
for k in ks:
  print k


s = u"Steven！我是以前上海的John，還記得嗎？」路德伸出右手和Steven寒暄，只見Steven一面皺著眉頭，狐疑地看著路德，卻還是禮貌性的也伸出右手和他一握，接著就倒在吧台上。\n \n幾個小時後，Steven勉強張開了沈重的雙眼，發現自己全身被扒光，五花大綁在椅子上，「這是哪裡？你們是誰？放開我！」Steven一面吼叫，一面露出了驚恐的表情。\n「他的衣服有丟了吧？」路德對伊娜說。\n「如果裡面的追蹤器剛剛沒有被我踩爛，現在應該也是跟著垃圾車滿街跑。」伊娜說。\n僵持了2個小時又更好碰到晚餐時間，大家都累了，這時一個年紀50幾歲的大叔，推著快速爐和一大堆食材走了進來。\n \n「小朋友們，餓了嗎？」大叔一說完，就先把豆豉和大蒜下鍋炒香，還故意拿了風扇把香氣往Steven身上吹，只見Steven不安地扭動著身體。\n「接著我們加絞肉還有醬油！」只見大叔拿著湯匙舀起了醬油，從鍋邊淋了下去。\n「白飯！我要白飯！」凡登像是小朋友一樣開心的跳著。\n「有有有，香噴噴的北海道七星米正在電鍋裡燜！」大叔好像在安撫小朋友一樣對著凡登說。\n另外一頭，已經24小時沒有進食的Steven，開始顯露出不不耐煩的表情。\n「想要再請問一下Steven，你是RAB特務嗎？」路德站在電扇後面，一面用手把香氣往電扇裡送，香氣，像是無形的彈雨一樣，讓早已飢腸轆轆的Steven快要招架不住。\n「讓我猜猜，Kingzman?」Steven忽然變臉，露出了詭異的笑容。\n「果然是RAB特務！」伊娜驚訝的說。\n「為什麼"
kk = re.split(unicode("[(\\r)|(\\n)|\s|。|！|？|「|」|...|?|!|,|，]"),s)
for k in kk:
  print k


jieba.set_dictionary('/home/aha/Project/NewsInsight/src/lab/dict/dict.txt.big')
jieba.load_userdict("/home/aha/Project/NewsInsight/src/lab/dict/user_dict.txt")
jieba.analyse.set_stop_words("/home/aha/Project/NewsInsight/src/lab/dict/user_stop_words.txt")
jieba.analyse.set_idf_path("/home/aha/Project/NewsInsight/src/lab/dict/idf.txt.big")




words = jieba.cut(data["content"], cut_all=False)
for word in words:
    print word

import jieba.posseg as pseg
words = pseg.cut(data["content"])
for w in words:
    print('%s %s' % (w.word, w.flag))

words = pseg.cut("|現年|63|歲|的|立法會|議員|黃毓民|於|去年|年|7|月|3|日|襲擊|特首|梁振英|".replace("|",""))
for w in words:
    print('%s %s' % (w.word, w.flag))




