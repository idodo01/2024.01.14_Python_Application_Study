from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    
    data = []
    
    while len(data) < n :
        data.append(randint(1,45))
        data = list(set(data))
        
        # 리스트 자료형을 set(리스트)를 통해서 
        #set 타입으로 변경하면서 중복을 제거합니다.
        
        #그 후에 list(set(리스트)) 다시 리스트로 감싸주어서 
        #리스트 타입으로 데이터를 변경합니다.

    return data

# 테스트 코드
print(generate_numbers(6))