#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open("D:/devtest/python/newfile.txt", 'w')
for i in range(1, 11):
    data = u"%d번째 줄입니다.\n" % i
    f.write(data)

f.close()
