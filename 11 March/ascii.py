# ABCD  ascill values = A= 65 B= 66 C 67  a97 b 98 c99 0=48 1=49 2=50
# EFGH
# IJKL
# MNOP 
# WHY WE REQUIRE ASCII = charector in binary
# ascii value depends on character size 
# chr function changes to charcater 
n=65
for i in range(1,5):   
     for j in range(1,5):
        print(chr (n),end="\t")
        n=n+1
     print()    
