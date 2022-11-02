import doubleagent
import random
import pyperclip
from multiprocessing import Process, Queue


# main = ['대용량', '식약처인증', 'suffling']
# keyword = ['유산균', '프로바이오틱스', ]
# sub = ['포스트', '사과', '러쉬', '더티', '퍼퓸', '캬라멜', '돼지고기']
def autionmaker(main, keyword, sub, autionmaker_result):
    main.append('suffling')

    counterer = 0

    # main.append('suffling')

    prefinal_list = []
    while True:
        counter = 0
        keyword_list = []
        main_list = []
        middle_list = []
        while True:
            # print(main_list)

            if counter == 6:
                break
            main = doubleagent.mix(main)
            if counter == 0 and main[0] == '대용량':
                continue
            if counter == 1 and main[0] == '대용량':
                continue
            if main[0] == 'suffling':
                keyword = doubleagent.mix(keyword)

                main_list.append(keyword[0])

                filteredkeyword = keyword[1:]
                counter = counter + 1
                filteredkeyword = doubleagent.mix(filteredkeyword)

                keyword_list.append(filteredkeyword)
                continue
            main_list.append(main[0])
            keyword = doubleagent.mix(keyword)

            keyword_list.append(keyword)
            counter = counter + 1

        for l1, l2 in zip(main_list, keyword_list):
            two = ' '.join(l2)
            middle = l1 + ' '+two
            middle_list.append(middle)
        if doubleagent.overlapchecker(middle_list) == True:

            continue
        else:
            break
    ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  성능정하의 원인
    cool = []

    i = 0
    while i < len(sub)+1:

        t = doubleagent.speedcases(sub, i, 2)

        for li in t:

            cool.append(li)
        i = i+1

    cool = cool[1:]

    lst2_list = []

    #  성능정하의 원인
    for i, middle in enumerate(middle_list):
        all = []
        if i < 2:
            space = 50
        if i > 1:
            space = 46

        #  성능정하의 원인

        for li in cool:

            narrow = []

            u = middle+' '+' '.join(li)

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

        lst2 = lst2[:6]
        for li in lst2:
            li = ' '.join(li)

        lst2 = doubleagent.mix(lst2)

        lst2_list.append(lst2[0])

    counter = 0

    for middle, lst2 in zip(middle_list, lst2_list):
        lst2 = ' '.join(lst2)
        if counter < 2:
            prefinal_list.append(middle + ' '+lst2)

        if 1 < counter < 4:
            prefinal_list.append(middle + ' ' + lst2 + ' 2통')

        if 3 < counter < 6:
            prefinal_list.append(middle + ' ' + lst2 + ' 3통')
        counter = counter + 1
    autionmaker_result.put(prefinal_list)
