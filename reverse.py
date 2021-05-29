n=int(input('enter number'))
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10

print("reverse is %d"%(rev))

      
#enter number12345
#reverse is 54321
