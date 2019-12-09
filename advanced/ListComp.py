#List Comprehensions

#要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
list(range(1, 11))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#如果要生成[1x1, 2x2, 3x3, ..., 10x10]，方法一：for循环
L = []
 for x in range(1, 11):
    L.append(x * x)

# L
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#方法二，列表生成式：
#把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
[x * x for x in range(1, 11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

[x * x for x in range(1, 11) if x % 2 == 0]
#[4, 16, 36, 64, 100]

#还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
	print(k, '=', v)

#y = B
#x = A
#z = C


#列表生成式也可以使用两个变量来生成list：

d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()]
#['y=B', 'x=A', 'z=C']

#把一个list中所有的字符串变成小写：

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
#['hello', 'world', 'ibm', 'apple']