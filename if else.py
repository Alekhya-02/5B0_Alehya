name=input("Enter input")#string value
age=int(input("Enter age"))#integer value
if age<=18:
      print("SORRY!",name)
      print("You are NOT ELIGIBLE for Vote")
else:
      print ("HELLO",name)
      print ("you are ELIGIBLE for vote due to")

#expected output
#Enter input Harry
#Enter age 18
#HELLO Harry
#you are ELIGIBLE for vote due to 18

#Enter input Mr.potter
#Enter age 8
#SORRY! Mr.potter
#You are NOT ELIGIBLE for Vote
     
