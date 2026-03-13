# plaindrome 
no=int(input("eneter no: "))
rev=0
temp=no
while(no>0):
    rem=no%10
    rev=rev*10+rem
    no=no//10


if temp==rev:
    print("palindrome")
else:
    print("not palindrome ")
     

#Write a Python program to take a user's name and age as input and print a message like: