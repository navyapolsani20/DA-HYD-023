"""#task-1
user = input("enter the string:")
methods = [user.upper(),user.lower(),user.capitalize(),user.title(),user.swapcase()]
for i in methods:
    a = user.upper()
    print(a)
    b = user.lower()
    print(b)
    c = user.capitalize()
    print(c)
    d = user.title()
    print(d)
    e = user.swapcase()
    print(e)
    f = user.isupper()
    print(f)
    g = user.islower()
    print(g)
    h = user.istitle()
    print(h)
    break
print("PYTHON IS FUN and Learning Python".isupper())
print("PYTHON IS FUN and Learning Python".islower())
print("PYTHON IS FUN and Learning PYthon".istitle())

#task-2
user_name = input("enter the string:")
while user_name != "exit":
    if user_name.isalnum():
        print("username contains only letters and numbers")
    if user_name[0].isalpha():
        print("username begins with a letter")
    if user_name.isidentifier():
        print("Valid Python Identifier")
    if user_name.isascii():
        print("characters")
    else:
        print("null")
    user_name = input("enter the string")"""

#task-3

print("-" * 80)
print("STUDENT REPORT".center(80))
print("-" * 80)

for i in range(3):
    student_name = list(map(str,input("Enter the name:" ).split(",")))
    marks = list(map(int,input("Enter the marks: ").split(',')))

    if marks >= 80 and marks <= 100:
        grade = "A Grade"
    elif marks >= 60:
        grade = "B Grade"
    elif marks >= 40:
        grade = "C Grade"
    else:
        grade = "Fail"

    print(f"{student_name.ljust(20)} {str(marks).center(10)} {grade.rjust(15)}")


