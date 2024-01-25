# open('파일명', 'r or w')
# r: read, w: write
with open('chicken.txt', 'r') as f :
    for line in f:
        print(line)