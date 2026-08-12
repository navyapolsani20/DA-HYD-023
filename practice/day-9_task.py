"""#calculate the price of total products
#i/p = 1200,1500,1600,1800
product = list(map(int,input("enter the price:").split(',')))
total = 0
for i in product:
    total = total + i
print(total)


password = input()
upper = lower = digit = special = 0
for i in password:
    if("A" <= i <= "Z"):
        upper += 1
    elif("a" <= i <= "z"):
        lower += 1
    elif("0" <= i <= "9"):
        digit += 1
    else:
        special += 1
print("upper:",upper)
print("lower:",lower)
print("digit:",digit)
print("special:",special)"""


a = input().split()
for i in a:
    print(i.split("@")[1])



