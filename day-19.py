'''
functions --> arguments Usage(variable length arguments)
          -->keyword variable length arguments(*kwargs)
Exception handling // scope of variables // built-in functions

exception Handling -->It is a mechanism that helps to respond or make the flow of
execution in a normal way,without this errors will occur and disrupt the flow of program

Common exceptions --> valueError,TypeError,IndexError,AttributeError,ZeroDivisionError
Syntax:

try:
    #code that will cause the exception
except Exception as e:
    #code will catch the exception
finally:
    #runs irrespective of try/except..
    
#basic Exception handling
try:
    #a = 10
    #a = int(input("enter the value:"))
    a = [10,20,30]
    #result = 20/a
    print(a[5])
except Exception as e:
    print(e)   #it returns the message of the error
except ValueError: #check by changing case
    print(f'Invalid entry enter only integer value:')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of varaible properly')
except IndexError:
    print(f'Indexing is out of range')
    
#similarly if we want to check other Errors -->IndexError,AttributeError
try:
    a = [10,20,30]
    a.apped(24)
    print(a[4])
#except Exception as e:
    #print(e)
except IndexError:
    print(f'check the length of the list properly and access the elements')
except AttributeError:
    print(f'dont rush check the name properly')

try:
    a =[10,20,30]
    a.apped(24)
    print(a[5])
except (IndexError,AttributeError) as e:
    print(e)
    a = list(map(int,input("enter").split(',')))#only for understanding
    print(a)
#BMI --> bmi = (weight) / ((height)**2)
#feet --> 12 inches-->1 inch --> 2.54cm
while True:
    try:
        weight = int(input("enter the weight in kgs"))
        height = float(input("enter the height in meters"))
        #write logical condition
        if weight > 0 and height > 0:
            break #stops the flow of execution of program
            #continue #skips the current iterationa and proceed for rmng iteration
            #print("bye")
        else:
            print("make sure enter only correct values")
    except ValueError:
        print("Make sure enter the weight as only integers only,and enter height in intergers")
bmi = (weight)/((height)**2)
print(bmi)

#use exception handling along with jumping statenets in functions BMI task
'''
#scope of variables --> Scope is basically the region/area where it is accessible
#Local scope,Global scope
#usage of global keyword,Enclosing Scope(Nested Functions nonlocal keyword)

'''
local scope --> variables defined inside the function accessible inside

def display():
    "usage of local scope"
    name = "Codegnan" #local variable
    print(name)
display()
#print(name) #it raises NameError

#Global scope Variables  -->defined outside and can be accessible everywhere
#in the script

place = "hyd"
def display():
    """usage of global variable"""
    name = "codegnan"
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

count = 30
def data():
    """usage of global keyword"""
    global count
    count = count + 5
    print(f'Value inside the function is {count}')
data()
print(f'value outside the function is {count}')

#local variable has high priority over global variable
count = 20
def data():
    """priority of local vs global variable"""
    count = 5 #local variable
    count = count + 5
    print(f'Value inside the function is {count}')
data()
print(f'value outside the function is {count}')

#Enclosing scope (nonlocal keyword)

def outer():
    """Outer Function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10
        print(f'value inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()'''
#Built-in Functions  --> variable Builtin functions
len = 60
print(len + 4)

print(len("codegnan")) #TypeError -->Never evre use Builtin Functions as identifiers


    
           
    

