#using  loop
no=int(input("eneter no: "))
sum=0
while(no>0):
 x=no%10 
 sum = sum +x
 no=no//10
    
print("sum no  is ",sum)