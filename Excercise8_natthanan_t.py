username=input("usernmae :")
password=input("password :")
if username=="eng2545" and password=="1234":
    print("----WELCOME to DK SHOP----")
    print("รายการสินค้า")
    print("1.แอปเปิ้ล ราคา  : 30 บาท")
    print("2.มะละกอ ราคา  : 45 บาท")
    print("3.กล้วย   ราคา  : 20  บาท")
    print("4.ส้ม    ราคา  : 25 บาท")
    print("กรุณาเลือกหมายเลขสินค้า")
    Select=int(input(">>"))
    if Select==1:
        print("กรุณาใส่จำนวนสินค้า")
        number = int(input(">>"))
        print("ราคารวมทั้งสิ้น", number * 30, "บาท")
        print("--THANK YOU--")
    elif Select==2:
        print("กรุณาใส่จำนวนสินค้า")
        number=int(input(">>"))
        print("ราคารวมทั้งสิ้น",number*45,"บาท")
        print("--THANK YOU--")
    elif Select == 3:
        print("กรุณาใส่จำนวนสินค้า")
        number = int(input(">>"))
        print("ราคารวมทั้งสิ้น", number * 20, "บาท")
        print("--THANK YOU--")
    elif Select == 4:
        print("กรุณาใส่จำนวนสินค้า")
        number = int(input(">>"))
        print("ราคารวมทั้งสิ้น", number * 25, "บาท")
        print("--THANK YOU--")
else:
    print("รหัสไม่ถุกต้อง กรุณาลองใหม่")
