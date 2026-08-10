
"""secret="121"
while True:
    a=input("enter the number:")
    if secret==a:
        print("your secret number is:",a)
        break
    else:
        print('incorrect please try again')

secret = 123
guess = int(input())
while guess != secret:
    if guess < secret:
        print("too low")
    else:
        print("too high")
        guess = int(input())
        print("correct guess")

        
#task -->otp verification  
OTP = "950299"
curr_attempt = 0
max_attempts = 7
while curr_attempt < max_attempts:
    a = input()
    if (a == OTP):
        print("access gained")
        break
    else:
        remaining = max_attempts - curr_attempt
        print(f"wrong otp and you have only {remaining} attempts")
        print("try again")
        curr_attempt += 1
else:
    print("wait for 30 mins")


food = input()
count = 0
while food != "exit":
    count += 1
    food = input()
print("Total no of items ordered:",count)"""

secret = "python"
curr_attempt = 0
prev_attempt = 0
max_attempts = 3
while curr_attempt < max_attempts:
    a = input()
    if(a == secret):
        print("access gained")
        break
    else:
        remaining = max_attempts - prev_attempt
        print(f'wrong guess and you have only {remaining} attempts')
        curr_attempt += 1
else:
    print("chances over")
