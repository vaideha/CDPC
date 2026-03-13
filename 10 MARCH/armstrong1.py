#for i in range(1,10000):
 ### temp=no

# count logic 
#count=0
#while(no>0):
 #   no=no//10
  #  count+= 1
no = temp
while(no>0):
    rem=no%10
    sum =sum + rem**count
    no=no//10
    

if temp==sum:
    print("armstrog" , i)

