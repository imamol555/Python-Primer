def lcm(num1,num2):
	if num1>num2:
		num1, num2 = num2, num1
	for i in range(num2, num1*num2+1, num2):
		if i%num1 == 0:
			return i

print(lcm(4,17))