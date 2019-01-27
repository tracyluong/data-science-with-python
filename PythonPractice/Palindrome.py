# Write a function that accept a string as a single argument
# and print out whether that string is a palindrome.
# (A palindrome is a string that reads the same forwards and backwards.)
# For example, "abcddcba" is a palindrome, "1221" is also a palindrome.

# Approach 1:
def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

# Approach 2: (one-liner code)
# def palindrome(s):
#    return len(s) < 2 or s[0] == s[-1] and palindrome(s[1:-1])


# Ask user to enter a string
testString = input("Enter a string: ")

if palindrome(testString):
    print('%s is a palindrome' % testString)
else:
    print('%s is not a palindrome' % testString)
