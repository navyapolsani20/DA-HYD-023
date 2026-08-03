#Grade Checker
marks = int(input("enter the student marks :"))
if(marks>0 marks>=100):
    print("Invalid Marks entered")
elif(marks>=90 and marks<=100):
    print("Grade : A")
    print("Remarks : Outstanding!")
elif(marks>=80 and marks<=89):
    print("Grade : B")
    print("Remarks : Excellent!")
elif(marks>=70 and marks<=79):
    print("Grade : C")
    print("Remarks : Good")
elif(marks>=60 and marks<=69):
    print("Grade : D")
    print("Remarks : Fair,needs improvement")
elif(marks>=50 and marks<=59):
    print("Grade : E")
    print("Remarks : Poor,needs serious improvement")
else:
    print("Grade : F")
    print("Remarks : Failed,needs to reappear")

#Even-Odd Checker
num = int(input("enter the number:"))
if(num == 0):
    print("Zero is neither even nor odd")
elif(num<0 and num % 2 == 0):
    print("Negative Even Number")
elif(num<0 and num % 2 == 1):
    print("Negative Odd Number")
elif(num>0 and num % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")

#season Identifier
month = int(input("enter the month number:"))
if(month>12):
    print("Invalid month entered")
elif(month == 12 or month == 1 or month == 2):
    print("Season:Winter")
elif(month == 3 or month == 4 or month == 5):
    print("Season:spring")
elif(month == 6 or month == 7 or month == 8):
    print("Season:Summer")
else:
    print("Season:Autumn")
            

            
