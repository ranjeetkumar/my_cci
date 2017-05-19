
"""
Given two strings, write a method to decide if one is a permutation
of the other
"""
from collections import Counter

def check_permutation(str1,str2):
	if len(str1) != len(str2)
		return False
	c = Counter(str1)
	for char in str2:
		c[char] -= 1
	for value in c.values():
		if value != 0:
			return False
	return True


