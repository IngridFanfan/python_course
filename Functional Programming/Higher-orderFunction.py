#Higher-order function

#函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

#map/reduce

#map
#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
	return x * x

#r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#list(r)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

#reduce
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#比方说对一个序列求和，就可以用reduce实现：

from functools import reduce
def add(x, y):
	return x + y

#reduce(add, [1, 3, 5, 7, 9])
#25

#filter
#Python内建的filter()函数用于过滤序列。

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

#sorted
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

#sorted([36, 5, -12, 9, -21])
#[-21, -12, 5, 9, 36]

#sorted([36, 5, -12, 9, -21], key=abs)
#[5, 9, -12, -21, 36]

#sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
#['about', 'bob', 'Credit', 'Zoo']

#sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#['Zoo', 'Credit', 'bob', 'about']







