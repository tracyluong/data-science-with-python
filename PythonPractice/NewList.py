# Let’s say we have a list saved in a variable: a = [[1, 4], [9, 16], [25, 36]].
# Write one line of Python that takes this list a and makes a new list that contains [1, 4, 9, 16, 25, 36]

a = [[1, 4], [9, 16], [25, 36]]

b = [row[i] for row in a for i in range(2)]
print(b)
