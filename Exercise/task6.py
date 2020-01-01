#Task 6
# 斐波那契数列（Fibonacci sequence): Fn = F[n-1]+ F[n-2](n=>2)

n = int(input('Enter a number: '))
list = []

#Plan A:
def fib(n):
	a, b = 1, 1
	list.append(a)
	for i in range(1,n-1):
		a, b = b, a+b
		list.append(a)
	print(list)

#Plan B:
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

#Plan C:
def fib(n):
	if n == 1:
		list = [1]
	elif n == 2:
		list = [1,1]
	for i in range(2, n-1):
		list.append(fib(n-1), fib(n-2))

fib(n)