#check no is amrstrong 
#153= 1^3 + 5^3 + 3^3
   #   = 153
#** = power 
no=int(input("eneter no: "))
sum=0
temp=no

# count logic 
count=0
while(no>0):
    no=no//10
    count+= 1
no = temp
while(no>0):
    rem=no%10
    sum =sum + rem**count
    no=no//10
    

if temp==sum:
    print("armstrog")
else:
    print("not armstrong  ")
     
