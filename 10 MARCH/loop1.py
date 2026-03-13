#reverse of number using loop
no=int(input("eneter no: "))
rev=0
while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("reverse no  is ",rev)