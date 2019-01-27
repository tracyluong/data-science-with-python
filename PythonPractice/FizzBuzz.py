# Write code to print out 1 to 100.
# If the number is a multiple of 3, print out "fizz" instead of the number.
# If the number is a multiple of 5, print out "buzz".
# If the number is multiple of 3 and 5, print out "fizzbuzz".

for number in range(1,101):
    if number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    print(number)
