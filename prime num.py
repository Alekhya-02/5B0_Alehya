n=int(input('enter number:'))
i=2
Count=0
if(n==1):
    print('1 is neither PRIME NOR COMPOSITE')
elif(n<1):
    print("INVALID NUMBER")
else:
    while (i<n):
        if(n%i==0):
            Count+=1
            print("{} is not a prime number" .format(n))
            break
        i+=1
    if (Count==0):
        print("{} is a prime number" .format(n))

#enter number:11
#11 is a prime number

#enter number:6
#6 is not a prime number

#enter number:1
#1 is neither PRIME NOR COMPOSITE

#enter number:0
#INVALID NUMBER
