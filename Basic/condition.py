age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#Abkurzung:
if x:
    print('True')

#notice that input() is a str
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')