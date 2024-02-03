def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    
    i, j = 0, 0
    count_matching = 0
    
    while i < len(numbers) :
        while j < len(winning_numbers) :
            if numbers[i] == winning_numbers[j] :
                count_matching += 1
            j += 1
        j = 0    
        i += 1
    return count_matching    

print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))