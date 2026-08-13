"""list,Tuples

#list -> Mutable,Inordered,heterogenous
index(),count(),copy(),sort(),reverse()

details = ["Codegnan",7,2028,"Hyderabad"]
print(len(details))
print(details.index(7))
print(details.index("Codegnan"))
details.extend([7,21,45,21])
print(details.index(21))
print(details.index(21,6))
print(details.index("python"))#it returns ValueError

#task    
data = ["codegnan", "saketh", "python", "java"]
"for i in range(len(data)):
    print(i, ":", data[i])

for obj in data:
    print(data.index(obj),":",obj)

#copy()--> shallow copy of the given collection

new = data.copy()
print(new)
print(len(new))
print(type(new))
new[2] = "Agentic AI"
print(new)
print(data)
data.append("saketh")
print(new)
print(data)
new.extend(["navya","rao"])
print(new)
data = [1,4,5,[21,34,45],23]
print(data)
new = data.copy()
print(new)
new[3][2] = "agents"#whenevr we make changes in nested list original will be efected
print(new)
print(data)
new[1] = "python"
print(new)
print(data)

marks = [14,24,-45,27,35]
print(marks)
print(marks.sort())#returns None
print(marks)#it returns ascending order
marks.sort(reverse = True) # it returns descending order
print(marks)
marks.append("python")
print(marks)
#print(marks.sort()
#reverse()--> it returns revrese order
marks.reverse()
print(marks)
print(marks[::-1])
print(sorted("codegnan"))
#print(sorted("navya","minnu","76",98,45))
print(sorted("navya""minnu"))

#Tuples --> Tuples are Indeexed,heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notation

a =()
print(type(a))
print(len(a))

dim = 1.5,2.5
print(dim)
print(type(dim))"""

#operations --> Indexing,slicing,membership,striding,Merging,Repetition


courses = ("PFS","JFS",("DA","DS"),"AgenticAI",[100,6,6])
"""print(courses)
print(len(courses))
print(courses[-1][2])
print(courses[3][-2:])
#courses[2] = 23 #tuples are immutable
courses[-1].append("codegnan")
print(courses)
#create a nested tuple of above and work on slicing,Striding and list Function
print("PFS" in courses)
d = courses * 2 #repetition
print(d)
e = courses + [2,3,4,5]#merging
print(e)

#tuple is immutable --> count(),index()
print(courses.index("AgenticAI"))#returns first occurance
print(courses.count("agents:"))
#print(courses.sort()) #it returns an AttributeError --> sort() is in Lists not in Tuples
print(sorted(courses[-1]))
#print(sorted(coursses)) #as we have seen mixed type

#TypeCasting
d = tuple(sorted((23,12,3,4,5)))
print(d)

#evaluate()]
print("9+3")
print(eval("9+3"))
a = eval(input("enter the values"))
print(a)
print(type(a))"""

#task
#Take a user input as string,do this in two ways...
'''
1.give the count of each repeating character
test case: programming

g is repeating 2 times
m is repeating 2 times
r is repeating 2 times
2.
r is repating 2 times
index =[1,4]
m is repeating 2 times
index = [3,10]








