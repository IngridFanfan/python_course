#!/usr/bin/env python
# -*- coding: utf-8 -*-

#notes:
import os, random

#python 复合布尔表达式计算采用短路规则，即如果通过前面的部分已经计算出整个表达式的值，则后面的部分不再计算。如下面的代码将正常执行不会报除零错误：
a = 0
b = 1
if(a > 0) and (b/a > 2):
	print 'yes'
else:
	print 'no'

#而下面的代码就会报错：
#if ( a > 0 ) or ( b / a > 2 ):

#Python 没有 switch/case 语句，如果遇到很多中情况的时候，写很多的 if/else 不是很好维护，这时可以考虑用字典映射的方法替代:

def zero():
	return "zero"

def one():
	return "one"

def two():
	return "two"

def num2Str(arg):
	switcher={
	0:zero,
	1:one,
	2:two,
	3:lambda:"five"
	}

	func=switcher.get(arg, lambda:"nothing")
	return func()

if __name__ == '__main__':
	print num2Str(0)


#if 简单条件判断一行搞定：
a = [1, 2, 3]
b = a if len(a) != 0 else ""
print b

c = []
d = c if len(c) != 0 else "c is empty"
print d

#将列表中重复的数据放在后面，返回列表中元素去除重复后的个数：

def deduplication(nums):
	exist_nums = {}
	pointer = 0
	for num in nums:
		if num not in exist_nums:
			exist_nums[num] = True
			nums[pointer] = nums
			pointer += 1
	return pointer
print(deduplication([1,1,1,1,1,1,2,2,2,2,2,2,2,2]))

#找出排序数组的索引
def deduplication2(self, nums):
	for i in range(len(nums)):
		if nums[i] == self:
			print 'i: ', i
			return i
	#ich verstehe nicht, ab hier, was mit den Zeilen zu tun?
	i = 0
	for x in nums:
		if self > x:
			i += 1
	return i
print (deduplication2 (5, [1,3,5,6]))


#猜大小的游戏
s = int(random.uniform(1,10))
print 's: ', s
m = int(input('Enter a number:'))
while m != s:
	if m > s:
		print 'Too large'
		m = int(input('Enter a number:'))
	if m < s:
		print 'Too samll'
		m = int(input('Enter a number:'))
	if m == s:
		print 'Bingo!'
		break;

####### write my own code here! And the function above is not prefect#####

#猜拳小游戏:
while 1:
	s = int(random.randint(1, 3))
	if s == 1:
		ind = "Rock"
	elif s == 2:
		ind = "Scissor"
	elif s == 3:
		ind = "Paper"
	m = raw_input('Enter Rock, Scissor, Paper. Enter "End" end the game.')
	blist = ["Rock", "Scissor", "Paper"]
	if (m not in blist) and (m != 'End'):
		print "Wrong! Enter again!"
	elif(m not in blist) and (m == 'End'):
		print 'End the game'
		break
	elif m == ind:
		print "Tie!"
	elif (m =="Rock" and ind =="Scissor") or (m == "Scissor" and ind == "Paper") or (m == "Paper" and ind == "Rock"):
		print "You win!"
	elif (ind =="Rock" and m =="Scissor") or (ind == "Scissor" and m == "Paper") or (ind == "Paper" and m == "Rock"):
		print 'You lose!'


#Optimize the code above


