from unittest import case
MARKS=int(input("enter the MARKS : "))
match MARKS:
    case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
      print("A")
    case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
      print("B")
    case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
      print("C")
    case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 | 50 | 49 | 48 | 47 | 46 | 45 | 44 | 43 | 42 | 41 | 40:
      print("D")
    case _:
      print("FAIL")
