menulist=[]
pricelist=[]
totalprice=0
while True:
    menuname=input("please enter menu:")
    if menuname.lower()=="exit":
        break
    else:
        menuprice=int(input("price:"))
        totalprice += menuprice
        menulist.append(menuname)
        pricelist.append(menuprice)
def printbill():
    print("---eng shop---")
    for x in range(len(menulist)):
        print(menulist[x],pricelist[x])
    print("ราคารวมทั้งหมด:",totalprice)
printbill()

