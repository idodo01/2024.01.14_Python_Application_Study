from random import randint



def generate_numbers(n):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    data = []
    while len(data) < n :
        data.append(randint(1,45))
        data = list(set(data))
        
        # 리스트 자료형을 set(리스트)를 통해서 
        #set 타입으로 변경하면서 중복을 제거합니다.
        
        #그 후에 list(set(리스트)) 다시 리스트로 감싸주어서 
        #리스트 타입으로 데이터를 변경합니다.
    return data

def draw_winning_numbers():
    # 랜덤 7 숫자 뽑는 함수 : generate_numbers(7)
    data = generate_numbers(7)
    
    # 보너스 값 제외하고
    # index 0부터 시작(0 1 2 3 4 5 6)
    data_bonus = data.pop(6)
    
    # 리스트 정렬 후 마지막에 보너스 값 재추가
    data.sort()
    data.append(data_bonus)
    
    return data

print(draw_winning_numbers())