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


#MATCH STATEMENTS
MARKS=int(input("ENETR YOUR MARKS : "))
match MARKS: 
    case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
        print("A")             
    case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
        print("B")  
    case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
        print("C")
    case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 | 50 | 49 | 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 36 | 35 | 34 | 33:
        print("D")
    case _:
        print("FAIL")