for i in range(1, 10000):
    no = i
    sum_val = 0
    temp = no

    count = 0
    while(no > 0):
        no = no // 10
        count += 1
    
    no = temp
    while(no > 0):
        rem = no % 10
        sum_val = sum_val + rem**count
        no = no // 10
        
    if temp == sum_val:
        print("Armstrong", i)