'''#multi assigining variables
name,age,email_id = 'navya','21','navyapolsani20@gmail.com'
print(name)
print(age)
print(email_id)
print(name,age,email_id)
#name,age = navya,22,26 too many values to unpack
#reassinging variables
name = "codegnan"
a,b = 20,30
print(a,b)
a,b = b,a
print(a,b,sep=',')
#a,b = b,c
#print(a,b)#valueError where c is not definded
#deleting the variables -->del
#del a
print(a)
#del a,b
print(a,b)
#punctuators --> [](list),{}(dict,sets),()(tuples)
name = 'codegnan';age = '7';course = 'data analytics'
print(name,age,course)

#data types = Numeric(int,float,complex,boolean,Null,
            #---> sequences --> lists,tuples,sets,strings,frozensets,mappings(dict)
#numeric type =int,float,complex
#int datatype -->quantity,age
age = 7
print(age)
print(type(age)) #type --> returns the datatype of object
print(type(7))
#quantity = 01,It is not allowed
#print(quantity)

#float datatype = temp,salary,price
price = 750.35;discount = 2.5
print(price,discount)
print(type(price))
print(type(discount))

#complex datatype --> combination of real and imaginary
#data = 5 + 2i#invalid decimal iteral
#print(data)

data = 5 + 2j #j is for representation
print(data)
print(type(data))

#boolean datatype --> True / False

valid = True
print(type(valid))
error = False
print(type(False))

#type casting  --> converting one type to another type
#python by deafult follows : Implicit Type (we need not mention the datatype)
#we will go for Explicit Conversion

#every built in datatype is a builtin function
#int --> typecasting --> float,complex,bool
age = 22
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
#float --> typecasting --> int,complex,bool
price = 4300.35
print(type(price))
c = int(price)
print(type(c))
d = complex(price)
print(d)
e = bool(price)
print(e)
#complex --> typecasting --> int,float,bool
data = 2 + 5j
#print(type(data))
#a = int(data)
#print(a)#type error
b = bool(data)
print(b)
age = 45
a = int(float(bool(age)))
print(a)
b = bool(int(float(45)))
print(b)

a = 45 + 2.5 + 2 +7j + False
print(a)

