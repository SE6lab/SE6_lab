Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def fact(N):
  F = 1
  for i in range(1,N+1):
    F *= i
  return F
def sqrt(x):
    return math.sqrt(x)


print("Select operation.")
print("1.add")
print("2.subtract one number from another")
print("3.multiply")
print("4.divide")
print("5.sqrt")
print("6.factorial")


while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5','6'):
        if choice == '1':
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            num1 = int(input("Enter first number: "))
            print("Square root of  ", num1, "is ", square(num1))
        elif choice == '6':
	    num1 = int(input("Enter first number: "))
            print("Factorial ", num1, "is ", factorial(num1))

        break
    else:
        print("Error")
