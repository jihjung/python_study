#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

coffee = 10
while True:
    money = int(raw_input("돈을 넣어 주세요: ".encode(sys.stdout.encoding)))
    if money == 300:
        print(u"커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print(u"거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print(u"돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(u"남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print(u"커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
