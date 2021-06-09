def vatcalculate(totalprice):
    result=totalprice+(totalprice*7//100)
    return result
price=(int((input("price:"))))
print("totalprice:",vatcalculate(price))