num = int(input("Enter a number: "))
check = int(input("Enter the divide number: "))

if num % check == 0:
    print("This number is divisible by check")
else:
    print("This number is not divisible by check")

# if num % 2 == 0:
#     if num % 4 == 0:
#         print(f"The number {num} is even and a multiple of 4")
#     else:
#         print(f"The number {num} is even")
# else:
#     print(f"The number {num} is odd")