# reverse the num
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
rev = n1*10000+n2*1000+n3*100+n4*10+n5*1
print(rev)
# 5 digit reverse hw 
# also check the code 