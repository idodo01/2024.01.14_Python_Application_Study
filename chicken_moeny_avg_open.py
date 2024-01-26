with open('data/chicken.txt','r') as f:
    for line in f:
        money_list = line.strip().split(': ')
        print(money_list[1])
    