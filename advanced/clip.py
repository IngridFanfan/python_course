L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
r.append(L[i])
#r
#['Michael', 'Sarah', 'Tracy']

#slice:
L[0:3]
#Or:  L[:3]
#['Michael', 'Sarah', 'Tracy']

L[-2:-1]
#['Bob']

#A tuple is also a list, except that it is immutable. Therefore, a tuple can also be manipulated by slicing, but the result is still a tuple
(0, 1, 2, 3, 4, 5)[:3]
#(0, 1, 2)

#The string 'XXX' can also be thought of as a list, with each element being a character. Therefore, a string can also be sliced, but the result is still a string:
'ABCDEFG'[:3]
#'ABC'