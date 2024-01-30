with open('vocabulary.txt', 'w', encoding='utf-8') as f:

    while true :
        inputText_eng = input("영어 단어를 입력하세요: ")
        
        if inputText_eng == 'q' : 
           break

        inputText_kor = input("한국어 뜻을 입력하세요: ")
        
        if inputText_kor == 'q' : 
           break
       
       f.write('{}: {}\n'.format(inputText_eng, inputText_kor))
        
    
    
