def findPrime(n):
    primeCount = 0
    if n == 0 or n == 1:
        print(f"{n} is not a prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            primeCount += 1
    if primeCount == 0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

num = int(input("Please enter a number: "))
findPrime(num)