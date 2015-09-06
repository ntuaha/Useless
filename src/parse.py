#encoding=utf-8
import os
import datetime
import psycopg2
import sys
sys.path.append('/home/aha/Other_Project/jieba/')
reload(sys)
sys.setdefaultencoding('utf8')
import datetime

import jieba
import jieba.analyse
import json
from StringIO import StringIO
import re
import jieba.posseg as pseg





def run(d):
  with open("/home/aha/Project/Useless/data/%s.txt"%d,"r") as f:
    lines = f.readlines()
    total_cnt = len(lines)
    for i in xrange(0,total_cnt,3):
        #一個文件的開始，每三行一個文件
        line = lines[i]
        io = StringIO(line)
        data = json.load(io)
        data["title"] = lines[i+1]
        data["content"] = lines[i+2]
        #切出句子出來
        sentenses = re.split(unicode("[(\\r)|(\\n)|\s|。|！|？|「|」|...|?|!|,|，]"),data["content"].decode('utf-8'))
        k=False
        for s in sentenses:
          ss = re.search(unicode("(\d+)歲(.+)"),s)
          #沒找到就跳過
          if ss is not None:
            k=True
          else:
            continue
          #找出歲數
          age = int(ss.groups()[0])
          #初始化讀出名詞
          readN = False
          noun = None
          words = pseg.cut(s)
          r = ''
          for w_pair in words:
            #找到有歲就開始
            r = r+"%s[%s]|"%(w_pair.word,w_pair.flag)
            if w_pair.word =='歲':
              readN = True
            #找到有名詞屬性就結束
            if readN == True and 'n' in w_pair.flag:
              noun  = w_pair
              readN = False
              #寫出至檔案
              with open("/home/aha/Project/Useless/sentense2.log","a+") as f2:
                #print noun
                f2.write("%d:[%d-%s-%s]||%s"%(i,age,noun.word,noun.flag,r))
                for w in words:
                  f2.write("%s[%s]|"%(w.word,w.flag))
                f2.write("\n")
              with open("/home/aha/Project/Useless/sentense3.log","a+") as f3:
                f3.write('%s,%d,"%s","%s"\n'%(d,age,noun.word,noun.flag))

        if k==True:
          #break
          pass

#初始化  去除已經有的記錄檔
def initial():
  os.system('rm /home/aha/Project/Useless/sentense2.log')
  os.system('rm /home/aha/Project/Useless/sentense3.log')
  with open("/home/aha/Project/Useless/sentense3.log","a+") as f3:
    f3.write('date,age,word,flag\n')

if __name__ == "__main__":
  initial()
  for i in xrange(30):
    d = datetime.datetime(2015,8,i+1)
    print d
    run(d.strftime("%Y%m%d"))


