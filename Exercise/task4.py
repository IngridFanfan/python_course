#Task 4
#输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('Please enter a year: '))
month = int(input('Enter a month:'))
day = int(input('Then a day:'))

months = [0,31,59,90,120,151,181,212,243,273,304,334]

if month > 0 and month < 13:
	days = months[month - 1]
else:
	print('false month!Enter again!')
	month = int(input('Enter a month:'))

days += day

if year > 1000 and year < 2500:
	if year % 4 == 0:
		leap = True
	else:
		leap = False
else:
	print('false year! Enter again!')
	year = int(input('Please enter a year: '))

if leap and month > 2:
	days += 1

print ('The day is: ', days)