"""
 Implement a method to perform basic string compression 
 using the counts of repeated characters.  For example, 
 the string a a b c c c c c a a a would become a2blc5a3. 
 If the "compressed" string would not become smaller than 
 the original string, your method should return the original string.
"""

def compresion(str1):
    temp = []
    prev = None
    continuous_count = 1
    len_str1 = len(str1)
    finalstring = None
    for index in range(len_str1):
        if index+1 != len_str1 and str1[index] == str1[index+1]:
            continuous_count += 1   
        else:
            temp.append(str1[index]+str(continuous_count))
            continuous_count = 1
    finalstring = "".join(temp)
    if len(finalstring) < len_str1:
        return finalstring
    else:
        return str1