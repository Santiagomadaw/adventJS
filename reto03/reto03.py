def findNaughtyStep(original, modified):
    def diference(str1, str2):
        if str2 == '':
            return str1[0]
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                return str1[i]
        
        return str1[-1]
    
    if len(original)> len(modified):
        return diference(original,modified)
    elif len(modified)> len(original):
        return diference(modified,original)
    else:
        return []

original = 'iiiii'
modified = 'iiiii'
print(findNaughtyStep(original, modified))