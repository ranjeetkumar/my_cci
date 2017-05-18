"""
Implement an algorithm if a string has all unique characters 
What if you cannot use additional data structures
"""
#Brute force implementation without using any data structures
def brute_is_unique(string):
    stringlen = len(string)
    for i in range(stringlen):
        for j in range(i+1, stringlen):
            if string[i].lower() == string[j].lower():
                return False            
    return True

def optimize_runtime_unique(string):
    if len(string) > 128:
        return False
    char_presence = [False for _ in range(128)]
    for char in string:
    	# get the interger value of the char
        val = ord(char)
        if char_set[val]:
            return False
        #set the correspondence index to True
        char_presence[val] = True
    return True


