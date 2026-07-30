"""#input function
age = input
print(age)
a = int(input("enter the age :"))
print(a)
print(type(a))
b = float(input("enter the age :"))
print(b)
print(type(b))
c = str(input("enter the name :"))
print(type(c))
a = input().split()
print(a)
b = input().split(',')
print(b)
marks = list(map(int,input("enter the values :").split(',')))
print(marks)
marks = list(map(int,input("enter the values :").split()))
print(marks)
# now we have to input 2 values
age,salary = map(int,input("enter the values :").split(','))
print(age)
print(salary)
marks = list(map(float,input("enter the values :").split(',')))
print(marks)

#operators --> arthmetic,assignment,comparision,logical,membership,bitwise,identity
#arthmetuc operations --> +,-,*,/(float value),%(returns remainder),
#//(float division)---> returns quotient
a = int(input("enter a first number :"))
b = int(input("enter a second number :"))
c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)
g = a % b
print(g)
h = a // b
print(h)
#area of rectangle
length = int(input("enter a number:"))
breadth = int(input("enter a number:"))
area = length * breadth
print(area)
#area of square
side = int(input("enter the number:"))
area = side * side
print(area)
#area of triangle
breadth = int(input("enter a number:"))
height = int(input("enter a number:"))
area = 1/2 * breadth * height
print(area)
# assignment operator --> =,+=,-=,*=,/=

a=30
print(a)
#update the number
a = a+10
print(a)
a += 30
print(a)
a -= 30
print(a)
a *= 30
print(a)
a /=  30
print(a)
#comparision operator --> ==,>(greater than),<(less than),!=(not equal),>=,<=
a = 40
print(a == 40)
print(a > 4)
print(a < 400)
print(a != 470)
print(a >= 67)
print(a <= 76)
#membership operator -->in,not in(it checks for the existence of an object in a collection)
#it gives true or false
marks = [67,89,90,56]
print(35 in marks)
print(89 in marks)
print(5 not in marks)"""
names = "navya","minnu","jyo"
print("navya" in names)
print("ya" in names)
#logical operator --> AND,OR,NOT -->decision making
#AND--> all should true
#OR --> any one can true
a = (25 in [25,30]) and 20<30
print(a)
#identity operator -->is,is not
#they check for identity of an object --
a = 78
b = 67
print(a is b)
print(id(b))
print(id(a))


