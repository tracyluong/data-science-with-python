# Write a program to calculate sum of two numbers
# If sum in the range of (15,20), return 20
# If not, return the actual sum


def calculate(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("Result is: ", calculate(num1, num2))
