def factorial (n):
    number = 1
    for i in range (1, n + 1):
        number *= i
        print(f"factorial {i}: {number}")

user_input = int(input("enter the number to see factorial of: "))
factorial(user_input)

