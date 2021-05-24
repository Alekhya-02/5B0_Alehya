amt=int(input('enter bill amount'))
if (amt>=1000 and amt<2000):
    print('Total bill is',amt)
    dis=amt*10/100
    print('Discount on the billed amount is ',dis)
    bill=amt-dis
    print('paid bill :',bill)
else:
    if (amt>=2000 and amt<3000):
        print('Total bill is ',amt)
        dis=amt*20/100
        print('Discount on the billed amount is',dis)
        bill=amt-dis
        print('paid bill : 1600')
    elif(amt>=3000 and amt<5000):
        print('Total bill is',amt)
        dis=amt*30/100
        print('Discount on the billed amount is ',dis)
        bill=amt-dis
        print('paid bill :',bill)
    elif(amt>=5000):
        print('Total bill is',amt)
        dis=amt*40/100
        print('Discount on the billed amount is ',dis)
        bill=amt-dis
        print('paid bill :',bill)
    else:
        print('SORRY!')
        print('please purchase above 1000 to get the discount')
    
#expected output
#enter bill amount1200
#Total bill is 1200
#Discount on the billed amount is  120.0
#paid bill : 1080.0

#enter bill amount2300
#Total bill is  2300
#Discount on the billed amount is 460.0
#paid bill : 1600

#enter bill amount3400
#Total bill is 3400
#Discount on the billed amount is  1020.0
#paid bill : 2380.0

#enter bill amount5500
#Total bill is 5500
#Discount on the billed amount is  2200.0
#paid bill : 3300.0    

#enter bill amount400
#SORRY!
#please purchase above 1000 to get the discount    

    

    
