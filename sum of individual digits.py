#USING WHILE LOOP
n=123
sum=0
while(n>0):
    r=n%10
    sum += r
    n//=10
    
print(sum)

"OUTPUT = 6"

#USING FOR LOOP
n=123
sum=0
for r in str(n):
    r=n%10
    sum += r
    n//=10
    
print(sum)

"OUTPUT = 6"

