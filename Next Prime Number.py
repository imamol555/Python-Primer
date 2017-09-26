#########################
#Title - Generate Next Prime Number
#Author -  Amol Patil
#########################


def main():
    currentprime = 2
    while True:
        choice = input("Generate next prime ?\t Y/N ")
        if(choice == 'y' or choice =='Y' ):
            print(currentprime)
            currentprime = generatePrime(currentprime)
        elif(choice == 'n' or choice =='N'):
            break
        else:
            print("Please enter Y/N")

def generatePrime(num):
    newPrime = num+1
    while True:
        if(not isPrime(newPrime)):
            newPrime +=1
        else:
            break
    return newPrime
def isPrime(num):
    if(num%2 ==0):
        return False
    for i in range(3,int(num**0.5)+1, 2):
        if(num%i == 0):
            return False
    return True

if(__name__ =='__main__'):
    main()


