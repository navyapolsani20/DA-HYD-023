"""string -->case conversion,Searching and Finding,string testing methods
replace,space removal"""

"""# searching and finding,replacing,joining..
name = "Navyarao"
print(len(name))
print(min(name))
print(max(name))
b = name.index("y")#it returns the index position
print(b)
c = name.index("a")#it retuns the first occurance
print(c)
d = name.index("a",2)#it returns the next occurance
print(d)
e = name.index("a",1,9)
print(e)
print("Navyarao".count("a"))
print("Navyarao".count("w"))
#e = name.index("p")#valueError
#print(e)
#f = name.index("a",9)
#print(f)

#rindex -->it returns last occurance
a = name.rindex("y")
print(a)
b = name.rindex("a")
print(b)
c = name.rindex("a",8)#returns valueError
print(c)

#find()-->first occurence but it avoid error returns -1 if substring is not found
print("navya".find("r")) #it returns -1
print("navya".find("v")) #it returns as index
print("navya".rfind("a")) #it returns last occurance
print("navya".find("a")) #it returns first occurance
a = "datanalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))

#replacing,splitting,joining..

#strings are immutable
a = "navya"
print(a.replace('n','k'))
print(a)
b = a.replace("n","k")
print(b)

print("#navya#rao#polsani".replace("#"," "))
a = "navya"
b = (a.replace("k","n"))

a = "code navya python"
print(len(a))
b = a.split()#by deafult if we have space it splits(returns list)
print(b)
print(len(b))

c = "code,navya,python"
d = c.split()
print(d)
print(len(d))
e = c.split(",")
print(e)
print(len(e))

#join() --> concatenate any number of strings

a = "navya"
b = "rao"
print(a.join(b))
print(b.join(a))
print("@".join("navya"))
print("navya".join("@"))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...
a = "navyarao123"
print(a.isalnum()) # it returns True for alphanumeric strings else False
b = "navyarao"
print(b.isalnum())
print(b.isalpha())#returns True for only alphabets
print(b.isdigit())#returns True for only digits
print("12345".isdigit())
print("12345".isnumeric())#this has upper edge (numbers,functions,romans)
print("Navya".startswith("N"))
print("Navya".startswith("v",2))
print("Navya".endswith("a"))
print("Navya".endswith("v",1,3))
a ="navya"
print(a.islower())#returns True for all lower cases
b = "NAVYA"
print(b.isupper())#returns True for all upper cases
print("Navya Rao".istitle())
print("Navya rao".istitle())

#space removal --> strip() (removes leading and trailing spaces)
a = " navya "
print(a.strip())
b = input("enter the string:").strip().lower()
print(b)"""
#zfill  --> filling with zeroes as per the given numeric string
print("234".zfill(6))
print("78965".zfill(3))
#center(),ljust(),rjust() --> alignment of strings (check length and then simplify
#it with accordingy
print("hi".center(6))
print("hi".center(6,"#"))
print("hi".ljust(6,"#"))
print("hi".rjust(6,"%"))




