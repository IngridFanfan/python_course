#Iteration迭代 for ... in

#As long as it is an iterable object, it can be iterated with or without subscripts. For example, dict can iterate:
d = {'a': 1, 'b': 2, 'c': 3}
 for key in d:
     print(key)

#By default, dict iterates over the key. If you want to iterate over value, use "for value in d.values()", 
#and if you want to iterate over both key and value, use "for k, v in d.items()".

#Since strings are also iterable objects, they can also operate on for loops:

for ch in 'ABC':
	print(ch)


#How do you determine if an object is an iterable object? The method is judged by the Iterable type of the collections module:
 
#from collections import Iterable
#isinstance('abc', Iterable) # str是否可迭代
#True
#isinstance([1,2,3], Iterable) # list是否可迭代
#True
#isinstance(123, Iterable) # 整数是否可迭代
#False

# Python's built-in "enumerate" function turns a list into an index-element pair so that both the index 
#and the element itself can be iterated through the for loop:
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)


for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)