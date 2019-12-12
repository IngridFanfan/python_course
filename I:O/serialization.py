#serialization
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

#把一个对象序列化并写入文件：

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d
#{'age': 20, 'score': 88, 'name': 'Bob'}

#JSON
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
#'{"age": 20, "score": 88, "name": "Bob"}'

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
#{'age': 20, 'score': 88, 'name': 'Bob'}

#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
import json

class Student(object):
    def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s))