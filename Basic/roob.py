#!/usr/bin/python
# -*- coding: UTF-8 -*-
if True:
	print("Answer")
	print("True")
else:
	print("Answer")
	print("False")

#raw_input("按下 enter 键退出，其他任意键显示...\n")

count = 100
miles = 1000.0
name = "John"

print count
print miles
print name

a = b = c = 1
a, b, c = 1, 2, "John"
print a, b, c

#Python有五个标准的数据类型：Numbers（数字）, String（字符串）, List（列表）, Tuple（元组）, Dictionary（字典）
#Python支持四种不同的数字类型：int（有符号整型）, long（长整型[也可以代表八进制和十六进制]）, float（浮点型）, complex（复数）

#String
s = 'abcdef'
print s[1:5]
#'bcde'

str = 'Hello World!'
 
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str[3:]       # 输出从第四个字符开始的字符串
print str * 2       # 输出字符串两次
print str + 'Test'  # 输出连接的字符串

#Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print letters[0:6:2]
#['A', 'C', 'E']

#List
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

#['runoob', 786, 2.23, 'john', 70.2]
#runoob
#[786, 2.23]
#[2.23, 'john', 70.2]
#[123, 'john', 123, 'john']
#['runoob', 786, 2.23, 'john', 70.2, 123, 'john']

#Tuple 
#元组不能二次赋值，相当于只读列表。

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第四个（不包含）的元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组

#('runoob', 786, 2.23, 'john', 70.2)
#runoob
#(786, 2.23)
#(2.23, 'john', 70.2)
#(123, 'john', 123, 'john')
#('runoob', 786, 2.23, 'john', 70.2, 123, 'john')

#以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
#list[2] = 1000     # 列表中是合法应用

#Dictionary
#列表是有序的对象集合，字典是无序的对象集合。

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
 
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

#This is one
#This is two
#{'dept': 'sales', 'code': 6734, 'name': 'john'}
#['dept', 'code', 'name']
#['sales', 6734, 'john']


#=======================Opertaion==================
a = 21
b = 10
c = 0
 
c = a + b
print "1 - c 的值为：", c
 
c = a - b
print "2 - c 的值为：", c 
 
c = a * b
print "3 - c 的值为：", c 
 
c = a / b
print "4 - c 的值为：", c 
 
c = a % b
print "5 - c 的值为：", c
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print "6 - c 的值为：", c
 
a = 10
b = 5
c = a//b 
print "7 - c 的值为：", c

#Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
print 1/2
#0
print 1.0/2
#0.5
print 1/float(2)
#0.5

#========== assignment ============
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100
print "1 - c 的值为：", c
 
c = a | b;        # 61 = 0011 1101 
print "2 - c 的值为：", c
 
c = a ^ b;        # 49 = 0011 0001
print "3 - c 的值为：", c
 
c = ~a;           # -61 = 1100 0011
print "4 - c 的值为：", c
 
c = a << 2;       # 240 = 1111 0000
print "5 - c 的值为：", c
 
c = a >> 2;       # 15 = 0000 1111
print "6 - c 的值为：", c


#========== logic ==============
a = 10
b = 20
 
if  a and b :
   print "1 - 变量 a 和 b 都为 true"
else:
   print "1 - 变量 a 和 b 有一个不为 true"
 
if  a or b :
   print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "2 - 变量 a 和 b 都不为 true"
 
# 修改变量 a 的值
a = 0
if  a and b :
   print "3 - 变量 a 和 b 都为 true"
else:
   print "3 - 变量 a 和 b 有一个不为 true"
 
if  a or b :
   print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "4 - 变量 a 和 b 都不为 true"
 
if not( a and b ):
   print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
   print "5 - 变量 a 和 b 都为 true"



# ============ Others ============
# in, not in, is, is not
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
 
if ( a in list ):
   print "1 - 变量 a 在给定的列表中 list 中"
else:
   print "1 - 变量 a 不在给定的列表中 list 中"
 
if ( b not in list ):
   print "2 - 变量 b 不在给定的列表中 list 中"
else:
   print "2 - 变量 b 在给定的列表中 list 中"
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print "3 - 变量 a 在给定的列表中 list 中"
else:
   print "3 - 变量 a 不在给定的列表中 list 中"


a = 20
b = 20
 
if ( a is b ):
   print "1 - a 和 b 有相同的标识"
else:
   print "1 - a 和 b 没有相同的标识"
 
if ( a is not b ):
   print "2 - a 和 b 没有相同的标识"
else:
   print "2 - a 和 b 有相同的标识"
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print "3 - a 和 b 有相同的标识"
else:
   print "3 - a 和 b 没有相同的标识"
 
if ( a is not b ):
   print "4 - a 和 b 没有相同的标识"
else:
   print "4 - a 和 b 有相同的标识"












