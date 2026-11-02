 #MENU CARD USING MATCH STATEMENTS
from unittest import case


DOSA=1
IDLI=2
VADA=3
UPMA=4
BONDA=5
ORDER=int(input("ENTER YOUR ORDER NUMBER :"))
match ORDER:
 case 1:
  print("1CHUTNEY \n2 SAMBAR \n3 CHUTNEY+SAMBAR")
  type=int(input("SELECT WITH WHAT SIDING YOU WANT US TO SERVE :"))
  match type:
    case 1:
        print("YOU HAVE ORDERED DOSA WITH CHUTNEY,THE PRICE IS ₹40")    
    case 2:
        print("YOU HAVE ORDERED DOSA WITH SAMBAR, THE PRICE IS ₹50")
    case 3:
        print("YOU HAVE ORDERED DOSA WITH CHUTNEY&SAMBAR, THE PRICE IS ₹60")
    case _:
        print("SORRY WE DON'T HAVE THAT TYPE OF DOSA")
 case 2:
  print("1CHUTNEY \n2 SAMBAR \n3 CHUTNEY+SAMBAR \n4 GHEE-KARAM \n5 GHEE-KARAM+CHUTNEY \n6 RAGI IDLI")
  type=int(input("SELECT WITH WHAT SIDING YOU WANT US TO SERVE :"))
match type:
    case 1:
        print("YOU HAVE ORDERED IDLI WITH CHUTNEY,THE PRICE IS ₹30")
    case 2: 
        print("YOU HAVE ORDERED IDLI WITH SAMBAR, THE PRICE IS ₹40")
    case 3:
        print("YOU HAVE ORDERED IDLI WITH CHUTNEY&SAMBAR, THE PRICE IS ₹50")
    case 4:
        print("YOU HAVE ORDERED IDLI WITH GHEE-KARAM, THE PRICE IS ₹50")
    case 5:
        print("YOU HAVE ORDERED IDLI WITH GHEE-KARAM&CHUTNEY, THE PRICE IS ₹60")
    case 6:
        print("YOU HAVE ORDERED RAGI IDLI, THE PRICE IS ₹100")
    case _:
        print("SORRY WE DON'T HAVE THAT TYPE OF IDLI")
 case 3:
  print("1CHUTNEY \n2 SAMBAR \n3 CHUTNEY+SAMBAR \n4 CHICKEN")
  type=int(input("SELECT WITH WHAT SIDING YOU WANT US TO SERVE :"))
match type:
    case 1: 
        print("YOU HAVE ORDERED VADA WITH CHUTNEY,THE PRICE IS ₹30")
    case 2:
        print("YOU HAVE ORDERED VADA WITH SAMBAR, THE PRICE IS ₹40")
    case 3:
        print("YOU HAVE ORDERED VADA WITH CHUTNEY&SAMBAR, THE PRICE IS ₹50")
    case 4: 
        print("YOU HAVE ORDERED VADA WITH CHICKEN, THE PRICE IS ₹100")
    case _: 
        print("SORRY WE DON'T HAVE THAT TYPE OF VADA")
case 4:
print("1CHUTNEY \n2 SUGAR")
type=int(input("SELECT WITH WHAT SIDING YOU WANT US TO SERVE :"))
match type:
    case 1:
        print("YOU HAVE ORDERED UPMA WITH CHUTNEY,THE PRICE IS ₹30")
    case 2:
        print("YOU HAVE ORDERED UPMA WITH SUGAR, THE PRICE IS ₹40")
    case _:
        print("SORRY WE DON'T HAVE THAT TYPE OF UPMA")
case 5:    
print("1CHUTNEY \n2 SAMBAR \n3 CHUTNEY")
type=int(input("SELECT WITH WHAT SIDING YOU WANT US TO SERVE :"))
match type:
        case 1:
            print("YOU HAVE ORDERED BONDA WITH CHUTNEY,THE PRICE IS ₹30")
        case 2:
            print("YOU HAVE ORDERED BONDA WITH SUGAR, THE PRICE IS ₹40")
        case _:
            print("SORRY WE DON'T HAVE THAT TYPE OF BONDA")
case _:
    print("SORRY WE DON'T HAVE THAT TYPE OF ORDER")