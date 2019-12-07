#generator生成器
#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

L = [x * x for x in range(10)]
#L
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
#g
#<generator object <genexpr> at 0x1022ef630>

#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
next(g)
#0
next(g)
#1
next(g)
#4

#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#正确的方法是使用for循环，因为generator也是可迭代对象：
g = (x * x for x in range(10))
for n in g:
	print(n)

#Fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

#注意，赋值语句：a, b = b, a + b 相当于：

#t = (b, a + b) # t是一个tuple
#a = t[0]
#b = t[1]

#Fibonacci with generator:
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#差别：函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。

