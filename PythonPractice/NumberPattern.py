# Write a program to print the number pattern using loop.
# 111111
# 22222
# 3333
# 444
# 55
# 6

import sys

rows = 6
num = 1
for x in range(rows, 0, -1):
 for y in range(0,x):
  sys.stdout.write(str(num))
  sys.stdout.flush()
 print()
 num = num + 1