
"""#write a python program to calculate the innings of a player and count thedot balls,
#boundaries and total count
player = [4,6,1,0,2,4,0,6]
total = 0
dot_balls = boundaries = runs = 0
for i in player:
    total = total + i
    if(i == 4 or i == 6):
        boundaries += 1
    elif(i == 0):
        dot_balls += 1
    else:
        runs += 1
print("boundaries:",boundaries)
print("dot_balls:",dot_balls)
print("runs:",runs)
print(total)"""
'''
#write a python program for ATM pin verification
pattern = "950299"
curr_attempt = 0
max_attempts = 5
while curr_attempt < max_attempts:
    a = input()
    if (a == pattern):
        print("access gained")
        break
    else:
        print("try again")
        curr_attempt += 1
else:
    print("phone is locked and try again after 30 mins")
'''
'''
user_name = "admin"
password = "123"
a = input("enter the user_name:")
b = input("enter the password:")
if(a == user_name):
    print("user_name is correct",user_name)
elif(b == password):
    print("password is correct",password)

correct_pin = 1234
count = 0
while count < 5:
    pin = int(input())
    if pin == correct_pin:
        print("Phone Unlocked")
        count = 5
    else:
        count += 1
if pin!= correct_pin:
    print("Phone locked")'''
    
"""correct_pin = 1568
count = 0
while count < 3:
    pin = int(input())
    if pin == correct_pin:
        print("access gained")
        count = 3
    else:
        count += 1
if pin != correct_pin:
    print("ATM is blocked")"""

movies = input("enter movie names:").split(',')
count = 1
for movie in movies:
    print(count,movie)
    count += 1
