def findFirstRepeated(gifts):
    first_index=len(gifts)
    for index in range(len(gifts)):
        for index2 in range(index+1,len(gifts)):
            if gifts[index] == gifts[index2] and index2 < first_index:
                first_index= index2
    if first_index != len(gifts): return gifts[first_index]
    else: return -1
            
    


def findFirstRepeated2(gifts):
    reviewed= []
    
    for gift in gifts:
        if gift in reviewed:
            return gift
        else:
            reviewed.append(gift)
    return -1
            
giftIds = []



def findFirstRepeated3(gifts):
    reviewed= []
    
    for gift in gifts:
        if gift in reviewed:
            return gift
        else:
            reviewed.append(gift)
    return -1
            
  


def findFirstRepeated4(gifts):
  
    
    for index in range(1,len(gifts)):
        print(index, gifts[index],gifts[:index])
        if gifts[index] in gifts[:index-1]:
            return gifts[index]
        
    return -1
giftIds = [2, 2]
firstRepeatedId = findFirstRepeated4(giftIds)     
print(firstRepeatedId)
