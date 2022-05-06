
import parmap
from multiprocessing import Manager
import doubleagent
import random
import pyperclip
from multiprocessing import Process, Queue
import multiprocessing


def multigo(tt):
    prefinal = tt[0]

    noselectedlst2 = tt[1]

    lst2_list = []

    cool = []
    all = []
    i = 0
    while i < len(noselectedlst2)+1:

        t = doubleagent.speedcases(noselectedlst2, i, 2)

        for li in t:

            cool.append(li)
        i = i+1

    space = 169
    cool = cool[1:]

    #  성능정하의 원인

    for li in cool:

        u = prefinal+' '+' '.join(li)

        if len(u.encode('euc-kr')) > space:

            continue

        # for q in sub:

        #     r = u + ' '+q

        #     if len(r.encode('euc-kr')) < space:
        #         narrow.append(False)
        #     else:
        #         narrow.append(True)

        # if doubleagent.unanimous(narrow, True) == True:
        all.append(li)

    all = doubleagent.mix(all)
    lst2 = sorted(all, key=len)
    lst2.reverse()

    # for li in lst2:
    #     li = ' '.join(li)

    lst2 = doubleagent.mix(lst2[:5])

    lst2_list.append(lst2[0])

    lst2_list = doubleagent.ll2l(lst2_list)
    lst2_list = ' '.join(lst2_list)
    coupang_list = prefinal + ' '+lst2_list
    return coupang_list
