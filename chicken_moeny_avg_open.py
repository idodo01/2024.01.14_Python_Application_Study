with open('data/chicken.txt','r') as f:

    chicken_list = f.readlines()
    
    i = 0 
    sum = 0
    
    while i < len(chicken_list) :
        
        chicken_money = chicken_list[i].strip().split(': ')
        sum += int(chicken_money[1])
        
        i += 1

    print(sum/len(chicken_list))
    
