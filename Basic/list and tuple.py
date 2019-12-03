#list and tuple

#list
classmates = ['Michael', 'Bob', 'Tracy']
classmates[2]
classmates[-1]

#adding to the end:
classmates.append('Adam')

classmates.insert(1, 'Jack')

#delete the end element:
classmates.pop()

classmates.pop(1)

#replace:
classmates[1] = 'Sarah'

L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']

p = ['asp', 'php']
sp = ['python', 'java', p, 'scheme']

#empty:
L = []



#tuple, A tuple cannot be modified once it is initialized
#no append(), no insert()
classmates = ('Michael', 'Bob', 'Tracy')
t = ()

#means there is only 1 element
t = (1,)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
# it will be modified as: ('a', 'b', ['X', 'Y'])
