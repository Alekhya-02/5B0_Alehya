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
    
    

    

    
