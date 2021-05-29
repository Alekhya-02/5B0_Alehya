num = int(input('enter number'))
i = 1
if(num<1):
    print('INVALID NUMBER')
else:
    while (i<=num) :
        if num%i==0:
            print("%d" %(i))
            i = i+1

#enter number100
#1
#2
#4
#5
#10
#20
#25
#50
#100
