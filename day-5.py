"""#using if keyword
eyword
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
        print("enter only +ve values greater than 0 and less than 100")
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

#task --> same case use if-elif-else keywords usage in another way

#voter eligibility check case --> make sure to satisfy all the conditions
#age>=18 -->"yes"
#age<18--->"no"
#negative values -->not acceptable

age=int(input("enter your age"))
if(age>=18 and age <=100):
    print("--user has vote eligibility")
    print("--access granted--")
elif(age<18 and age>0):
    print("--user is not eligible to vote")
else:
    print("use +ve values which is greater than 0 and less than 100")
#output-->print() --> we pass any values also sep and end
#output formatting --> old style formatting(using commas)
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "navya";place = "warangal"
print(name,place) #by default sep is having space
print(name,place,sep = ',')
print(name,place,sep = '----')
print(a,b,end ='\n')
print(a,b)"""
name = "codegnan";age=7;batch="DA_023";place="hyd"
#usage of commas
print(batch,"is in ",name)#variables and msg should be sep by commas
print(name,"is in",place,"age is ",age,"years")
#old style formatting --> %d = integer,%f = float,%s = string
salary = 2500.67
print("my salary %d"%(salary))
print("my salary %f"%(salary))
print("my salary %.1f"%(salary))
print("my salary %.2f"%(salary))

#. format usage
print("{} is in {}".format(name,place))#order matter

#fstring usage(name = recommended)
print(f"{name} is in {place}")





















