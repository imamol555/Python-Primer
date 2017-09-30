

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

def isDivisible(x, list):
	for i in range(0,len(list)):
		if(x % list[i] != 0):
			return False
	return True		

def lcm3(numlist):
	numlist.sort()
	worst = product(numlist)
	#print(worst)
	for x in range(numlist[-1], worst+1, numlist[-1]):
		if(isDivisible(x,numlist)):
			return x		
mylist = [3,2,16,17]

a = lcm3(mylist)
print(a)