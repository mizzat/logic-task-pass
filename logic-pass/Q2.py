#Note that I cheated at this one :/
def isPrime(num):
    if num>1:
        for count in range(2,int(pow(num,(1/2)))):
            if not(num%count):
                return False
                break
        return True
    else:
        return False


number=int(input("Type a number: "))
for count in range(0,number):
    if isPrime(count):
        print(count,end=',')
