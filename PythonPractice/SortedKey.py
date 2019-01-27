# Given a dictionary my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}.
# Write code to print out a list of sorted key based on their value.
# For example, in this case, the code should print out ['b', 'd', 'a', 'c']

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}

sorted_by_value = sorted(my_dict.items(), key=lambda x: x[1])
sorted_key = []

for item in sorted_by_value:
    sorted_key.append(item[0])
print(sorted_key)
