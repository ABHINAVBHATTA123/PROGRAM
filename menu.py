#forty-first program
DOSA=1
IDLI=2
VADA=3
ORDER=int(input("Enter your order number:  "))
if ORDER==1:
    print("You have ordered DOSA,the price is 50rs")
elif ORDER==2:
    print("You have ordered IDLI,the price is 30rs")
elif ORDER==3:
    print("You have ordered VADA,the price is 20rs")
else:
    print("Invalid order number")