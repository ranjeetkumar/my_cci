"""Given two strings, write a function to check if
they are one edit or zero edits away
"""

def oneedit(str1, str2):
    bigger_string = None
    position = 0
    diff_count = 0
    len1 = len(str1)
    len2 = len(str2)
    
    if abs(len1-len2) > 1 :
        return False
    
    if len1 > len2:
        bigger_string = "string1"
    else: 
        bigger_string = "string2"
        
    if bigger_string == "string1" and len1 != len2:
        for i in range(len(str1)): 
             if position<len2 and str1[i] != str2[position]:
                  diff_count += 1
             else:
                  position += 1
                            
    if bigger_string == "string2" and len1 != len2:
        for i in range(len(str2)):
             if position<len1 and str1[position] != str2[i]:
                  diff_count += 1
             else:
                  position += 1
    if len1 == len2:
        for i in range(len(str2)):
             if str1[i] != str2[i]:
                  diff_count += 1
        
    if diff_count>1:
        return False
    else:
        return True
        