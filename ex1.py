name = input("What is your name? ")
age = int(input("How old are you? "))
num = int(input("How many lines do you need? "))

for i in range(num):
    print(f"Hi,{name}, you will turn 100 in {2025+(100-age)}\n")