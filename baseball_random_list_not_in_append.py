from random import randint


def generate_numbers():
    numbers = []
    # 여기에 코드를 작성하세요

    while len(numbers) < 3 :
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 테스트 코드
print(generate_numbers())
