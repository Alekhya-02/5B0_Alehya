n=int(input('enter number:'))
i=2
Count=0
if(n<2):
    print("INVALID NUMBER")
else:
    while (i<n):
        if(n%i==0):
            Count=1
            print("{} is not a prime number" .format(n))
            break
        i+=1
    if (Count==0):
        print("{} is a prime number" .format(n))

#enter number:11
#11 is a prime number

#enter number:5
#5is not a prime number

#enter number:1
#INVALID NUMBER

#enter number:0
#INVALID NUMBER
