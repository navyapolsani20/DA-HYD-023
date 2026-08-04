"""work_log = 01,0,,1,1,1,0,1,0
#result_variable --> longest_streak
longest_streak = 0#target_variable
current_streak = 0
for day in work_log:
    if( day == 1 ):
        current_streak = current_streak + 1
        if(current_streak > longest_streak):
            longest_streak = current_streak
            print(longest_streak)
            break #it stops here...
    else:
        current_streak = 0#streak breakss
else:
    print(f"longest streak is :{longest_streak}

#for with else notifications
n =[0,0,0]
for notification in n:
    if (n == 1):
        print("unread notifications")
        break
else:
    print("all read")

#try to take notification from user -->list of integrates
n = list(map(int,input("enter the values").split(',')))
print(n)
for notification in n:
    if(n == 1):
        print("unread notifications")
        break
else:
    print("all read")
#while -->it relies on condition...it continues the loop until the condition is true
#syntax
while(condition):
    statement(s)
    ....
    ...
while(True):
    print("Yes")
    #it runs to infinite loop -->to stop this click ctrl c
#ctrl c gives keyboard interrupt
#for while we have to initialize the object and also the count value
i = 0
while(i<=10):
    print(i)
    i += 1
i = 0
while(10>=i):
    print(i)
    i -= 1
i = 0
while(i<=10):
    print(10 - i)
    i += 1"""
#banking scenario --->PIN authentication if more than 3 attempts
#account locked..
pin = ["1234"]
max_attempts = 3
curr_attempt = 0
while curr_attempt < max_attempts:
    a = input("enter the pin:")
    if(a == pin):
        print("access gained")
        break
    else:
        print("try again")
        curr_attempt += 1
else:
    print("try again after 24 hrs")

    



