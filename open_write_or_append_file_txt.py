# 파일 쓰기 write
# with open('new_file.txt', 'w') as f:

# 파일 이어쓰기 append
# 기존 파일이 없으면 w와 같은 기능 -> 파일 쓰기
#with open('new_file.txt', 'a') as f:
    
    
with open('new_file.txt', 'a') as f:
    f.write("Hello world! \n")
    f.write("My name is Codeit \n")
    
    
