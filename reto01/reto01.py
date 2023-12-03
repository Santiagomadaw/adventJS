def findFirstRepeated(gifts):
    first_index=len(gifts)
    for index in range(len(gifts)):
        for index2 in range(index+1,len(gifts)):
            if gifts[index] == gifts[index2] and index2 < first_index:
                first_index= index2
    if first_index != len(gifts): return gifts[first_index]
    else: return -1
            
giftIds = []
firstRepeatedId = findFirstRepeated(giftIds)     
print(firstRepeatedId)        
        