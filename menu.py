#forty-first program
DOSA=1
IDLI=2
VADA=3
ORDER=int(input("Enter your order number:  "))
if ORDER==1:
    print("1 sambar \n2 chetny  ")
    type=int(input("select type : "))
    if type==1:
        print("You have ordered DOSA with sambar,the price is 50rs")
    elif type==2:
        print("You have ordered DOSA with chettny,the price is 40rs")
    else:
        print("not there")
if ORDER==2:
    print("1 sambar\n2 chutney\n3 ghee-karam")
    type=int(input("select type : "))
    if type==1:
        print("you have ordered IDLI with sambar,the price is 40rs")
    elif type==2:
        print("you have ordered IDLI with chutney,the price is 30rs")
    elif type==3:
        print("you have ordered IDLI with ghee-karam,the price is 50rs")
    else:
        print("not available")

if ORDER==3:
    print("1 chutney \n2 sambar")
    type=int(input("select type : "))
    if type==1:
        print("You have ordered VADA with chutney,the price is 30rs")
    elif type==2:
        print("You have ordered VADA with sambar,the price is 40rs")
    else:
        print("not available")
    
else:
    print("Invalid order number")