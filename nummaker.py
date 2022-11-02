from multiprocessing import Process, Queue


def nummaker(call, nummaker_result):
    number = str(call)

    if ' ' == number[0]:
        number = number[1:]
    if ' ' == number[-1]:
        number = number[:-1]
    number_list = []

    number_list.append('a'+number)

    number_list.append('a'+number+str(-2))

    number_list.append('a'+number+str(-3))

    nummaker_result.put(number_list)
