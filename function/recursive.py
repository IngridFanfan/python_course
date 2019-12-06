#Recursive function

#factorial
#fact(n) = n x fact(n-1)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

#Take care to prevent stack overflow: Tail recursion
#Tail recursion is when a function calls itself when it returns, and the return statement cannot contain an expression.

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
