# 1. import 모듈 사용
# 같은 폴더의 파일을 불러와서 사용할수 있다
# 이와같은 파일을 모듈이라고 부른다

import calculator

print(calculator.add(2,5))
print(calculator.multiply(2,5))
# 2. import as
# 모듈을 호출할 때마다
# 길게 붙이는게 번거롭기에
# as 로 짧게 이름 지을 수 있다
import calculator as calc

print(calc.add(2,5))
print(calc.multiply(2,5))

# 3. from 으로 모듈의 함수 자체를 호출
from calculator import add, multiply

print(add(2,5))
print(multiply(2,5))

# 4. import * 로 전체 함수 불러오기
# from calculator import * 

# 함수명만 표기되기에
# 출처가 불분명해질 수 있다

# 필요한 함수만 불러오는 3. 과
# 짧은 이름이 표시되는 2. 를 추천한다
