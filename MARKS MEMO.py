# MARKS MEMO #
NAME=input("ENETR YOUR NAME : ")
CLASS=input("ENTER YOUR CLASS AND SECTION : ")
MARKS=int(input("ENTER YOUR MARKS : "))
if MARKS>=90:
    print(f"{NAME}\n{CLASS}\nGRADE ALLOTED : A")
elif MARKS>=80:
    print(f"{NAME}\n{CLASS}\nGRADE ALLOTED : B")
elif MARKS>=70:
    print(f"{NAME}\n{CLASS}\nGRADE ALLOTED : C")
elif MARKS>=60:
    print(f"{NAME}\n{CLASS}\nGRADE ALLOTED : D")
elif MARKS<60:
    print(f"{NAME}\n{CLASS}\n NO GRADE ALLOTED ")

    