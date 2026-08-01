#identify operator --->
"""
a = [1,2,3,4]
b = a
print(id(a))89
print(id(b))
c = [1,2,3,4]
print(id(c))
#as we know list is mutable collection both ca and a lists will have different
#ids whereas values are same
print(c is a)#output False
print(c == a)#ouput True
print(a is not c)#output True
#bitwise operators -->perform bitwise operations over operands
# &(and),|(or),^(XOR),shifting operators(<<,>>)
a = 5 & 3#number will be converted into binary format and bitwise and is performed
print(a)
print(5|3)#bitwise - OR
print(5^3)#bitwise - XOR
print(5 and 3)#here and is for logical operator which checks for existences returns
#5 in above case
print(5 or 3)
#left shift operator <<,right shift operator >>
print(5<<1)#left shift operation by one postion
print(5>>1)#right shift opertator by one position
print(4>>2)
print(4<<2)
print(15<<2)#convert 15 to binary and perform 2 timesleft shifting
print(2<<10)
#input formatting -->input(),int(input()),float(input())
#we know --> single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split(',')))
#tokens--> Numeric data types --> operators --> flow of the program
#control block statements
#when to execute,how to execute
#conditional statements --> if,else,elif(rely on condition to be executed)
#loop or repetition statements -->for ,while


#condtional statements--> if usage
syntax

if(condition):
    statements to be executed

#age = 15
age = int(input("enter your age:"))
if(age > 18):
    print("enter your age: ", age)

age = int(input("enter ur age:"))
if(age >= 18 and age in [20,23,24]):
    print("enter ur age:",age)
print(age)

#if - else keyword
#syntax
if(condition):
    statements to be execute...
else:
    statements....

#checking the eligibility to vote
age = int(input("enter your age:"))
if(age >= 18):
    print("you have eligibility to vote",age)
else:
    age = 18 - age
    print("you need to wait for more",age,"years")
#lets see only nested -->if,else
age = int(input("enter your age:"))
if(age > 0):
    if(age >= 18):
        print("you have eligibility to vote",age)
    else:
        age = 18 - age
        print("you need to wait for more",age,"years")
else:
    print("you entered negative values")
marks=int(input("enter the marks:"))
if(marks>90 and marks<100):
        print("A")
else:
        if(marks>80 and marks<90):
                print("B")
        else:
                if(marks>70 and marks<80):
                        print("C")
                else:
                        
                        if(marks>60 and marks<70):
                                
                                print("D")
                        else:
                                
                                if(marks>50 and marks<60):
                                        print("E")
                                else:
                                     print("Fail")
#using if keyword
marks = int(input("enter the marks : 1-100"))
if(marks > 0 and marks <= 100):
        if(marks>=90):
                print("user has secured Grade A")
        if(marks>=80 and marks<89):
                print("user has secured Grade B")
        if(marks>=70 and marks<79):
                print("user has secured Grade C")
        if(marks>=60 and marks<69):
                print("user has secured Grade D")
        if(marks<60):
                print("user has failed again")
else:
        print("enter only +ve values greater than 0 and less than 100")"""
#using if -else if keyword
marks = int(input("enter the student marks"))
if(marks >= 100):
        print("entered values should be greater than 1 and less than 100") 
elif(marks>=90 and marks<=100):
        print("user has secured Grade A")
elif(marks>=80 and marks<=89):
        print("user has secured Grade B")
elif(marks>=70 and marks<=79):
        print("user has secured Grade C")
elif(marks>=60 and marks<=69):
        print("user has secured Grade D")
elif(marks<60 and marks<=0):
        print("user has failed,study again")
else:
        print("enter only +ve values greater than 0 and less than 100")        
