my_string = "1, 2, 3, 4, 5"

# split
# 1. ","를 기준으로 나누기
print(my_string.split(","))

# 2. ", "를 기준으로 나누기
print(my_string.split(", "))

# 3. split는 list로 값을 나누어 담는다
my_string_data = my_string.split(", ")

# 각각 출력하려면 list[index]
print(my_string_data[0])
print(my_string_data[1])
print(my_string_data[2])
print(my_string_data[3])

# split도 화이트 스페이스 제거할 수 있다
# 파라미터를 넣지 않음 
print(my_string.split())
# strip는 앞뒤 화이트 스페이스 제거
# split는 사이사이의 화이트 스페이스 제거
