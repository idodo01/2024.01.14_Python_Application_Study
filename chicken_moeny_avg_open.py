with open('data/chicken.txt','r') as f:

    # readlines 한줄씩 리스트 값으로 만들어줌
    chicken_list = f.readlines()
    
    # print(chicken_list)
    
    i = 0 
    sum = 0
    
    while i < len(chicken_list) :
        
        # 함수 사용 이유
        # 1. 줄의 끝에 \n를 제거하기 위함 : strip()
        # 2. ': '를 기준으로 날짜와 매출 값을 분리함 : split(': ')
        
        # chicken_list[0] 은 '1일: 453400\n'
        # chicken_list[0].strip().split(': ')은 ['1일', '453400']
        # chicken_money[0]은 45340
        
        chicken_money = chicken_list[i].strip().split(': ')
        sum += int(chicken_money[1])
        i += 1

    print(sum/len(chicken_list))
    
