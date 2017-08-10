# -*- coding: utf-8 -*-
from random import randint

def divide2(total):
    print "\n--------分二"
    left = randint(1,total-1)
    right = total - left
    print "left : ", left
    print "right : ", right
    return [left, right]

def put1(left,right):
    print "\n--------掛一"
    right -= 1
    print "left :",left, "right :", right
    return [left, right]

def mod4(left, right):
    print "\n--------喋四"
    left_rem = left % 4
    if left_rem == 0:
        left_rem = 4
    right_rem = right % 4
    if right_rem == 0:
        right_rem = 4
    print "左餘 :",left_rem
    print "右餘 :",right_rem
    return [left_rem,right_rem]

def detect_ood(rem):
    print "\n--------歸奇"
    if (rem/4) -- 1:
        return 1
    else:
        return 0

def main():
    total = 50
    print "========大衍之數五十"
    print "total : ", total
    
    print "\n========其用四十有九"
    total -= 1
    taiji = 1
    temp = [0,0,0]
    print "total : ", total
    print "taiji : ", taiji

    #三變
    print "\n三變\n\n"
    for i in range(0,3):
       print "total :", total
       left, right = divide2(total)
       left, right = put1(left,right)
       left_rem, right_rem = mod4(left,right)
       rem = left_rem + right_rem
       print "叻 :", rem, "\n"
       total -= rem
       temp[i] = detect_ood(rem)

       if temp[i] == 1:
           print "奇"
       else:
           print "偶"
    
if __name__ == "__main__":
    main()