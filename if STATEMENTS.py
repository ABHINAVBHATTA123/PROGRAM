Age=17
if Age>=18:
    print("YOU ARE ADULT")
    print("YOU CAN VOTE")
    print("YOU CAN DRIVE")
else:
    print("YOU ARE A MINOR")
    print("YOU CANNOT VOTE")        
    print("YOU CANNOT DRIVE")

    is_logged_in = True

if is_logged_in:
  print("Welcome back!")
else:
    print("please log in ")

x=99
y=100
if x>y:
    print("x is greater than y")
elif x<y:
    print("x is less than y")
else:
    print("x is equal to y")


a=30
b=50
print("A") if a>b else print("B")


a=50
if a>30:
    if a>45:
        print("a<=>50")
else:
    print("a<50")