#use def to define a function

def new_abs(x):
	if x >= 0:
		return x
	else:
		return -x

#import a function from an external .py doc:
# from defFunc import new_abs 

#empty function
def skipMe():
    pass

#pass can be used in:
if age >= 18:
    pass

#return multiple values:
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#when running:
#x, y = move(100, 100, 60, math.pi / 6)
#print(x, y)