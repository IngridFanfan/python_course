# iterator迭代器
#可以使用isinstance()判断一个对象是否是Iterable对象:

from collections import Iterable
isinstance([], Iterable)
#True

#可以使用isinstance()判断一个对象是否是Iterator对象：

from collections import Iterator
isinstance((x for x in range(10)), Iterator)
#True

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：

isinstance(iter([]), Iterator)
#True
isinstance(iter('abc'), Iterator)
#True