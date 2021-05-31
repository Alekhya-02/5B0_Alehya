base = int(input('enter base:' ))
exponent = int(input('enter exponent:'))

result = 1

while (exponent != 0) :
    result = result * base
    exponent-=1
    remainder = result % 10

print("Answer = {}" .format(result))
print("the last digit is :{}".format(remainder))


#enter base:3
#enter exponent:4
#Answer = 81
#the last digit is :1

