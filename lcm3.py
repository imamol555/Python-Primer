#Title - Find the LCM of list of integers
#Author - Amol Patil
##############################################

#calculate the product of all items of a list
def product(list):
    p = 1
    for i in list:
        p *= i
    return p

#check if number is divisisble by all items in a list
def isDivisible(x, list):
	for i in range(0,len(list)):
		if(x % list[i] != 0):
			return False
	return True

#calculate LCM
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
