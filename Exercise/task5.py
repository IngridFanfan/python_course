#Task 5
#输入三个整数x,y,z，请把这三个数由小到大输出。

L = []
for i in range(0,3):
	x = int(input('Enter a number: '))
	L.append(x)

#遍历所有数组元素
for i in range(len(L)):
 
        # Last i elements are already in place
        for j in range(0, len(L)-i-1):
 
            if L[j] > L[j+1] :
                L[j], L[j+1] = L[j+1], L[j]



#Or just use: list.sort()
#Notice that, print(L.sort()) doesn't work

#L.sort()
print(L)