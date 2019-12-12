#StringIO和BytesIO

#StringIO顾名思义就是在内存中读写str。
from io import StringIO
f = StringIO()
f.write('hello')
#5
f.write(' ')
#1
f.write('world!')
#6
print(f.getvalue())
#hello world!

#getvalue()方法用于获得写入后的str。

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
		print(s.strip())

#Hello!
#Hi!
#Goodbye!

#BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
#6
print(f.getvalue())
#b'\xe4\xb8\xad\xe6\x96\x87'

#写入的不是str，而是经过UTF-8编码的bytes。

#可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
#b'\xe4\xb8\xad\xe6\x96\x87