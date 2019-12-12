#I/O operation

f = open('/Users/userName/test.txt', 'r')

#调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示:
f.read()
#'Hello, world!'

f.close()

#Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    print(f.read())

#如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
#你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')