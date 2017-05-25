"""
 Write a method to replace all spaces in a string with '%20'.
 You may assume that the string has sufficient space at the 
 end of the string to hold the additional characters, and that 
 you are given the "true" length of the string. Do it in place.
"""
def URLify(str1,len_str1):
	str1_list = list(str1)
	new_len_str1 = len_str1
	for index in range(len(str1_list)):
		if str1_list[index] == ' ':
			str1_list.append(' ')
			str1_list.append(' ')
			new_len_str1 += 2
	for reversed_index in range(len_str1-1, -1, -1):
		if str1_list[reversed_index] == ' ':
		    str1_list[new_len_str1-1] = '0'
		    str1_list[new_len_str1-2] = '2'
		    str1_list[new_len_str1-3] = '%'
		    new_len_str1 -= 3
		else:
		    str1_list[new_len_str1-1] = str1_list[reversed_index]
		    new_len_str1 -= 1
	return "".join(str1_list)



