# #         x^1  X^2  x^3 
# sum = a+ ----+----+-----+---n // series
           # 1    2     3 
n=int(input("enter n: "))
x=int(input("enter x: "))
sum =1 
for i in range (1,n):
    sum =sum+(x**i)/i
print(sum)