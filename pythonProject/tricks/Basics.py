# Remove repeated items from a list

numbers = [1, 2, 2, 3, 3, 3]
print(list(set(numbers)))
colors = ['blue', 'red', 'red', 'blue', 'red']
print(list(set(colors)))

# Zip Your Data
# You can group two iterable objects in Python with zip().
names = list(zip((1, 2), ['Anna', 'Alice']))
print(names)
names1 = list(zip(('Mrs', 'Mr'), ['Anna', 'Jack']))
print(names1)

# Reverse Lists
numbers1 = [1, 2, 3, 4, 5]
print(numbers1[::-1])
print(numbers1[:-1])
print(numbers1[-1])

s = "Hello"
print(s[::-1])

# Count all occurrences
from collections import Counter

numbers = [1, 1, 1, 2, 1, 4, 4, 4, 3, 6]
c = Counter(numbers)
print(c)

from collections import Counter

ch = "aabcaaabccaaaa"
c = Counter(ch)
print(c)

# Check Your Python Version
import sys

print(sys.version_info)

# Print your data with separators:
username = "user"
host = "mail.com"

print(username, host, sep="@")
print('25', '06', '2021', sep='-')

#Swap dictionary key & values:
mydict= {1: 11, 2: 22, 3: 33}
mydict = {i: j for j, i in mydict.items()}
print(mydict)


mydict= {'John': 'Tesla', 'Jane': 'BMW'}
mydict = {i:j for j,i in mydict.items()}
print(mydict)

# Get indexes of all letters from a string
s = 'Python'
e = enumerate(s)
print(list(e))

# Check if objects are the same with is & not is
t1 = ["Africa"]
t2 = ["Africa"]
t3 = t2
print(t1 is t2)
print(t1 is t3)
print(t1 is not t2)

# Concatenate tuples
colors = ('blue', 'red') + ('yellow', 'green')
print(colors)

numbers = (1, 2) + (3,) + (4, 5)
print(numbers)

# Use return instead of return None
def double(n):
     print(n * 2)
double(5)
print(type(double(5)))

def add_zero(l):
     l.append(0)
l = [1, 2, 3]
add_zero(l)
print(l)
print(type(add_zero(l)))