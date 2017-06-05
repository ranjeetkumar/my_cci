"""
Given two strings s1 and s2, write code to check if s2
is a rotation of s1 using only one call to isSubstring
"""
def rotation(str1,str2):
    if (str2 in (str1+str1) 
       and len(str1) == len(str2)):
        return True
    else:
        return False