import datetime

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))


# 오늘의 날짜
today = datetime.datetime.now()
print(today)
print(type(today))


# timedelta 타입
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day)) # timedelta 타입


# datetime 해부하기
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# datetime 포매팅
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

#%a	요일 (짧은 버전)	Mon
#%A	요일 (풀 버전)	Monday
#%w	요일 (숫자 버전, 0~6, 0이 일요일)	5
#%d	일 (01~31)	23
#%b	월 (짧은 버전)	Nov
#%B	월 (풀 버전)	November
#%m	월 (숫자 버전, 01~12)	10
#%y	연도 (짧은 버전)	16
#%Y	연도 (풀 버전)	2016
#%H	시간 (00~23)	14
#%I	시간 (00~12)	10
#%p	AM/PM	AM
#%M	분 (00~59)	34
#%S	초 (00~59)	12
#%f	마이크로초 (000000~999999)	413215
#%Z	표준시간대	PST
#%j	1년 중 며칠째인지 (001~366)	162
#%U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
#%W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35

