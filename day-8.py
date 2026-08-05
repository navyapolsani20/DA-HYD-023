"""#strings  -->group of characters ,we use single or double or triple quotes
# which represents of strings..
#strings are immutable,ordered,indexed collection

name = "Hyderabad"
print(name)
print(type(name))
print(len(name))

#index --->used to fetch the object(position)starts with 0 and ends at len(obj)-1
#index is represnted as []
print(name[4])
print(name[6])
#print(name[25]) #indexederror -->as it is out of trange

#Negative indexing --> -1 to len(obj)
print(name[-1]) #-->it returns last character
print(name[-6])

#slicing --> we can access group of characters(objects)
#we use [start:end]#start default -->0,start is included and end is excluded
name = "Warangal"
print(name[:])
print(name[0:])
print(name[:4])
print(name[1:5])
print(name[5:7])
print(name[2:6])
print(name[6:])
print(name[7:3])#-->returns empty as strings are immutable
#slicing is applicable for lower index to higher index
print(name[:67])#returns till the end of the string
#print(name[67])
#negative part
print(name[-5:-1])
print(name[-6:-3])
name = "python"
print(name[4:])
print(name[-2:])
print(name[-2:5])
print(name[1:-2])
#observe --.+ve_+ve,-ve_-ve,+ve_-ve all possibilites

#striving -->[start,end,step}

course = "DataAnalysis" 
print(course[::1])#returns all charcaters
print(course[::2])#includes start to end skipping 1 character
print(course[1:6:3])
print(course[2::3])

#negatuve striving

print(course[::-1])
print(course[::-2])
#task :workout with all possibilities of slicing and striving on a example

name = "codegnan"
#name[6]= "w"#strings are immutable
#alternative of stringgs --> Indexing,concatenation,repetition


print(name * 3)
print("%" * 10)
#combine strings = concatenation
data = "select" + "python" + " " + "database"
print(data)


for i in "codegnan":
    print(i,end=' , ')
for i in "name":
    print(i)

name = "Codegnan"
#built-in functions-->len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(max(name))
print(ord("C"))
print(ord("A"))
print(sorted(name))#returns list by sorting all elements"""

#multiple methods over strings-->case conversions,Finding/Searching
name ="Codeganan Data"
#case _conversion -->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
a = name.lower()
print(a)
a = name.title()
print(a)
#capitalize --> converts first letter to uppercase
a = name.capitalize()
print(a)

#Task: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Use loops and strings to return A-Z



