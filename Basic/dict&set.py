#dict & set

#dict, wie map(), （key-value）

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#（key-value）
d['Adam'] = 67

'Thomas' in d
#False

d.get('Thomas')
#if not exists, return none

d.get('Thomas', -1)
#or The specified value

d.pop('Bob')
#delete a key + value

#set, A collection of keys, but no value is stored. Since keys cannot be repeated, there are no duplicate keys in a set. 

s = set([1, 2, 3])

#Repeating elements are automatically filtered in the set:
s = set([1, 1, 2, 2, 3, 3])

s.add(4)

s.remove(4)

#Set can be regarded as a set of unordered and non-repeating elements in the mathematical sense. 
#Therefore, two sets can perform operations such as intersection and union in the mathematical sense:
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

s1 & s2
#{2, 3}
s1 | s2
#{1, 2, 3, 4}


#list & str
 a = 'abc'
b = a.replace('a', 'A')
print(b)
#'Abc'
print(a)
#'abc'