import doubleagent
import random
import pyperclip
from multiprocessing import Process, Queue


# allkey = {'firstkeywordaf':firstkeywordaf,'importantaf':importantaf,'subaf':subaf,'subimportantaf':subimportantaf}
def allmaker(allkey,limitinput, allmaker_result):
    limitinput =int(limitinput)
    firstkeywordaf = allkey['firstkeywordaf']
    connectedaf = allkey['connectedaf'] 
    importantaf = allkey['importantaf']
    print(connectedaf)
    counterer = 0
    timeout = 0
    counter = 0
    while True:
        conlistminus = []

        for i,first in enumerate(firstkeywordaf):
            
            connect = [x for x in connectedaf if x not in first]
            connectedoverlap = connect[:]
            connect = []
            first = ' '.join(first) 
            for li in connectedoverlap:
                lenfrist=len(first)
                if lenfrist == len(first.replace(li,'')):
                    connect.append(li)
            while True:
                # index = 'flag'
                # maxValue = len(important[0])
                # for i in range(0, len(important)):
                    
                #     if maxValue > len(important[i]):
                #         maxValue = len(important[i])
                #         index = i


                # if index == 'flag':
                #     index = 0

                conlength = len(first.encode('euc-kr'))
    
                pocket = 49 - (conlength)
                filterd = []
                for li in connect:
                    if len(li.encode('euc-kr')) < pocket:
                        filterd.append(li)
    
                if len(filterd) == 0:
 
                    conlistminus.append(first)
                    break
                keylist =doubleagent.mix(filterd)
                key = keylist[0]
                connect.remove(key)
                first = first+' '+key
                

        print(conlistminus)

        one = conlistminus[0].split(' ')
        two = conlistminus[1].split(' ')
        two = [x for x in two if x not in [' 2통']]
        three = conlistminus[2].split(' ')
        three = [x for x in three if x not in [' 3통']]
        if counter > limitinput:
            break
        if len([x for x in one if x not in two]) == 0:
            counter = counter + 1
            continue
        if len([x for x in one if x not in three]) == 0:
            counter = counter + 1
            continue
        if len([x for x in two if x not in three]) == 0:
            counter = counter + 1
            continue
        break

    while True:

        conlist = []

        for first in conlistminus:

            firstflag = first.split(' ')
            connect = [x for x in connectedaf if x not in first]
            connectedoverlap = connect[:]
            connect = []

            for li in connectedoverlap:
                lenfrist=len(first)
                if lenfrist == len(first.replace(li,'')):
                    connect.append(li)

            while True:


                conlength = len(first)

                pocket = limitinput - (conlength)
                filterd = []
                for li in connect:
                    if len(li) < pocket:
                        filterd.append(li)

                if len(filterd) == 0:

                    conlist.append(first)
                    break
                keylist =doubleagent.mix(filterd)
                key = keylist[0]
                connect.remove(key)
                first = first+' '+key


        break
        
        # allmaker_result.put(result)
    while True:

        conlist2 = []

        for first in conlist:

            firstflag = first.split(' ')
            important = [x for x in allkey['importantaf'] if x not in firstflag]
            connectedoverlap = important[:]
            important = []

            for li in connectedoverlap:
                lenfrist=len(first)
                if lenfrist == len(first.replace(li,'')):
                    important.append(li)

            while True:


                conlength = len(first)

                pocket = limitinput - (conlength)
                filterd = []
                for li in important:
                    if len(li) < pocket:
                        filterd.append(li)

                if len(filterd) == 0:

                    conlist2.append(first)
                    break
                keylist =doubleagent.mix(filterd)
                key = keylist[0]
                important.remove(key)
                first = first+' '+key


        break
        
        # allmaker_result.put(result)

    counter =0   
    while True:

        conlist3 = []

        for first in conlist2:

            firstflag = first.split(' ')

            subkey = [x for x in allkey['subimportantaf'] if x not in firstflag]

            while True:


                conlength = len(first)
  
                pocket = limitinput - (conlength)
                filterd = []
                for li in subkey:
                    if len(li) < pocket :

                        filterd.append(li)
                        # print(li)

                if len(filterd) == 0:

                    conlist3.append(first)
                    break
                keylist =filterd
                key = keylist[0]
                subkey.remove(key)
                first = first+' '+key
        break
    counter =0   

    while True:

        conlist4 = []

        for first in conlist3:

            firstflag = first.split(' ')

            subkey = [x for x in allkey['subaf'] if x not in firstflag]

            while True:


                conlength = len(first)
  
                pocket = limitinput - (conlength)
                filterd = []
                for li in subkey:
                    if len(li) < pocket :
                        print(pocket)
                        print(len(li))
                        filterd.append(li)
                        # print(li)

                if len(filterd) == 0:

                    conlist4.append(first)
                    break
                keylist =doubleagent.mix(filterd)
                key = keylist[0]
                subkey.remove(key)
                first = first+' '+key



        flag2 = doubleagent.listsplit(conlist4,2)
        
        one = conlist4[0].split(' ')
        two = conlist4[1].split(' ')
        two = [x for x in two if x not in [' 2통']]
        three = conlist4[2].split(' ')
        three = [x for x in three if x not in [' 3통']]
        if counter > limitinput:
            break
        if len([x for x in one if x not in two]) == 0:
            counter = counter + 1
            continue
        if len([x for x in one if x not in three]) == 0:
            counter = counter + 1
            continue
        if len([x for x in two if x not in three]) == 0:
            counter = counter + 1
            continue
        break
        
        # allmaker_result.put(result)
    result = [conlistminus, conlist4]
    allmaker_result.put(result)    
