"""sequence --> Strings,Lists,Tuples,Sets
Mapping -->dictionary

#list --> collection of heterogenous elements(item
list -->Indexed,Ordered,Mutable,heterogenous,we use [] to store the data

marks = [20,18,45,35,28]
print(marks)
print(len(marks))
print(type(marks))
print(35 in marks)
print(max(marks))
print(min(marks))

#operations --> Indexing,slicing,striding,membership,merging,repetition

#nested lisr --> list inside another list
names = ["Codegnan",25,8.09,[45,65,30,26],"DA23",34]
print(names)
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4])
print(names[0][4:])

#print the output of Cdga
print(names[0][::2])
names[0] = names[0][::-1]
print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,slicing --> Mutable
names[2] = "python"
print(names)
names[4] = ["navya","c","python","minnu"]
print(names)
print(len(names))
print(names[4][3])
print(names[4][2][2:])
print(names[4][2][::-1])

names[2:4] = "abhiram","sai","saketh","sai"
print(names)
print(len(names))
#In slicing whenevr elements is pass as per the logic length keeps on increasing
#print as folows:
#[codegnan,25,"abhiram","python","Saketh","Java","DA23",34]
names[3:6:2] = "python","java"
print(names)"""

#create a nested list with strings,lists and work on indexing ,slicing,striding
#added advantages if you could add string functions also to it
#list functions --> append(),insert(),pop(),extend(),remove(),clear(),index()
#count(),copy(),sort(),reverse()

names = ["codegnan","saketh"]
#append --> inserts single elements to the end of the list
names.append("data")
#print(names)
#names.append("analysis","agents")#TypeError
names.append(["analysis","agents"])
#print(names)
#names[3].append("chatgpt")
#print(names)
#print(names[3].append("chatgpt"))#it returns none as append is applicable
print(names)

#extend( )--> it also inserts multiple elements to the end of list
"""names.extend("analysis")
print(names)
names.extend(["analysis"])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45)#TypeError
#print(names)

#insert()(index,object)-->inserts giiven object before index
names.insert(1,"python")
print(names)
names.insert(0,"java")
print(names)
#names.insert([1:4],["a","b"])#invalid syntax
#print(names)
names.insert(-1,"AAA")
print(names)"""

#pop(),remove(),clear() -->
#pop()-->by default last,else given index
print(names.pop())
names.pop(2)
print(names)
#remove()--> we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
del names[1:3]#del keyword will apply permanent changes
print(names)
#clear()--. clear will remove all the elements in the list and returns empty list
names.clear()
print(names)

#data = ["codegnan","saketh","python","java"] #input
#output should be as follows
'''
0 : codegnan
1 : saketh
2 : python
3 : java

'''





