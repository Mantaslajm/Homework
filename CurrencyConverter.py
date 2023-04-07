
usd_to_Yuan_curency = 6.88


def usd_to_Yuan(usd_amount,exchange_fee=0):
    return round(usd_amount*usd_to_Yuan_curency+(usd_amount*exchange_fee),2)


def yuan_to_usd(yuan_amount,exchange_fee=0):

    return round(yuan_amount/usd_to_Yuan_curency+(yuan_amount*exchange_fee),2)

def  usd_to_Yuan_txt(usd_amount):
    yuan=usd_to_Yuan(usd_amount)
    txt=str(usd_amount)+" USD ="+ str(yuan)+" Yuan"
    return txt

def  yuan_to_usd_txt(yuan_amount):
    usd=yuan_to_usd(yuan_amount)
    txt=str(yuan_amount)+" Yuan ="+ str(usd)+" USD"
    return txt
print("2023-04-01 curency converting: ",usd_to_Yuan_curency)
###b

print(usd_to_Yuan_txt(1))
print(usd_to_Yuan_txt(1500))
print(usd_to_Yuan_txt(25000))

#####c

print(yuan_to_usd_txt(10))
print(yuan_to_usd_txt(1750))
print(yuan_to_usd_txt(25000))
