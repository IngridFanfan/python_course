#parameter

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#with default parameter: (Default parameters cannot be placed before required parameters)
#def power(x, n=2):

#Example:
def add_end(L=[]):
    L.append('END')
    return L

#add_end()
#['END']
#add_end()
#['END', 'END']
#add_end()
#['END', 'END', 'END']

#The default parameter must point to the invariant object
#Modify:
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


#Variable parameter
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#calc(1, 2)
#5

#Without *, input should be definded as list or tuple, like:
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#calc([1, 2, 3])
#14
#calc((1, 3, 5, 7))
#84

#Call a variable parameter:
#nums = [1, 2, 3]
#calc(*nums)
#14
#instead of: calc(nums[0], nums[1], nums[2])


#Keyword parameter
#Keyword arguments allow you to pass in 0 or any number of arguments with parameter names that are automatically assembled into a dict inside the function
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#person('Michael', 30)
#name: Michael age: 30 other: {}

#person('Bob', 35, city='Beijing')
#name: Bob age: 35 other: {'city': 'Beijing'}

#person('Adam', 45, gender='M', job='Engineer')
#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#extra = {'city': 'Beijing', 'job': 'Engineer'}
#person('Jack', 24, city=extra['city'], job=extra['job'])
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#extra = {'city': 'Beijing', 'job': 'Engineer'}
#person('Jack', 24, **extra)
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#Notice: **extra means that all key-values of extra dict are passed into the **kw parameter of the function with keyword parameters, 
#and kw will get a dict. Note that the dict obtained by kw is a copy of extra, and the change to kw will not affect extra outside the function.


#chekcing keyword parameters:
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


#Restrict the name of the keyword parameter
#Naming keyword arguments requires a special delimiter *, and the arguments following * are treated as named keyword arguments.

def person(name, age, *, city, job):
    print(name, age, city, job)
#person('Jack', 24, city='Beijing', job='Engineer')


#with default:
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
#person('Jack', 24, job='Engineer')


















