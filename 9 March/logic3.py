# sium of three digit no 

no=int(input("eneter any value"))
n1=no%10 #12345=5
no=no//10 #1234
n2 = no % 10  #4
no=no//10 #123 
n3=no%10  #3
no=no//10 #12 
n4 = no%10 #2 
no=no//10 # 2
n5 = no%10 #1 



res = n1+n2+n3 +n4+n5 
print(res)
# sum of five digint num hw 