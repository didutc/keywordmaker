from multiprocessing import Process, Queue


def pricemaker(originalprice, price, pricemaker_result):
    print(originalprice)
    print(price)
    originalprice = int(originalprice)
    price = int(price)
    originalprice = [str(originalprice), str(originalprice*2), str(originalprice*3)]
    finalprice = [str(price), str(round(round(2*price-3000-(price*0.07)),-2)), str(round(round(3*price-6000-(price*0.14)),-2))]

    pricemaker_result.put([originalprice, finalprice])
