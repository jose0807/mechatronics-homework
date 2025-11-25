name=input("please set your product:\n")
price= input("please set the price\n")
data = (f"product: {name.strip()} | price: ${price.strip()}")
try:
    cost=float(price)
    if cost <0 or len(name.strip())==0:
        print("please set a valid number or name")
    else:
        if len(data)==30:
            print(f"label:'{data}'")
        elif len(data)>30:
            print(f"label:'{data[:30]}'")
        elif len(data)<30:
            while len(data)<30:
                data=data+" "
            print(f"label:'{data}'")
except ValueError:
    print("please set a valid number")