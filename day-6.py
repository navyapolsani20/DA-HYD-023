"""#control statements -->controlthe flow of execution of the program
#                   -->conditional statements -->if,else,elif..
#                   -->repetition statements(loops) --> for,while(for with else)
#                                                       (while with else)
#                   -->Jumping statements --> break,continue,pass

#loop -->loops are helpful for repetition(Automative Tasks)
#for keyword will be helpful to iterate over a sequence / range
#syntax for for keyword):
""'for <temp_var> in sequence in range
    statement(S)...
range(start,stop,step)
By default range picks 0 as start value
for i in range(10):
    print(i)
#from above case we got 10 interactions:
for i in range(1,11):
    print(i)
    print(f"value of i is -->{i}")
    if i > 5:
        print(f"value of i is -->{i}")
#i want to get only even numbers with above condition
for i in range(1,10):
    if (i > 5 and i % 2 == 0):
         print(f"value of i is -->{i}")
#range(start,stop,step)--> here step internal...
for i in range(1,10,2):
    print(i)
for i in range(3,15,2):
    print(i)
for i in range(1,10,-1):
    print(i)
for i in range(-1,10,-1):
    print(i)
for i in range(10,1,-1):
    print(i)
for i in range(-10,0,1):
    print(i)
#--->useage in lists
names = ["navya","minnu","potti"]
print(len(names))#shows the length of names
for name in names:
    print(name)
    if (name == "minnu"):
        print(name)
#evaluate the sum of first 10 numbers
#understand your input -->range(11)-->10 numbers
#understand your output  --> sum(number)
#then we need to build the logic
result = 0
for i in range(11):
    print(i)
    result = result + i
    print(f"your result is : {result}")
#evaluate the sum of even upto 10
result = 0
for i in range(21):
    if (i % 2 == 0):
        result = result + i
        print(f"your result is : {result}")
#using step
result = 0
for i in range(0,21,2):
    if(i % 2 == 0):
        result = result + i
        print(f"your result is : {result}")"""
#understand the usage with fitness stream example
#work_in --> 1,work_out_missed -->0

work_log = 0,1,1,1,0,1,0
#result_variable --> longest_streak
longest_streak = 0#target_variable
current_streak = 0
for day in work_log:
    if( day == 1 ):
        print(day)
        current_streak = current_streak + 1
        if(current_streak > longest_streak):
            longest_streak = current_streak
    else:
        current_streak = 0#streak breakss
print(longest_streak)



        





















