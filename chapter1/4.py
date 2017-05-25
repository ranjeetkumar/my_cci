
"""
Given a string wrtie a function to check if 
it is a permutation of a palindrome
"""
from collections import Counter
def palindromeper(string):
    c = Counter()
    c.update(string.lower())
    odd_counter = 0
    for key, value in c.items():
        if value % 2 != 0 and key!=" ":
            odd_counter += 1
    if odd_counter >= 2:
        return False 
    else:
        return True
