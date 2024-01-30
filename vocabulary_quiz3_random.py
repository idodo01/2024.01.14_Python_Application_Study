import random
with open('vocabulary.txt','r') as f:

    # readlines 한줄씩 리스트 값으로 만들어줌
    vocabulary_list = f.readlines()
    
    
    while true :
        
        i = random.randint(1,len(vocabulary_list))
        
        vocabulary_value = vocabulary_list[i].strip().split(': ')
        
        # ocabulary_value[0]: 영어 단어
        # ocabulary_value[1]: 한글 
        
        input_eng = input('{}: '.format(vocabulary_value[1]))
        if input_eng == 'q':
            break
        elif input_eng == vocabulary_value[0] :
            print("맞았습니다!\n")
        else :
            print("아쉽습니다. 정답은 {}입니다.\n".format(vocabulary_value[0]))
        
        i += 1
    