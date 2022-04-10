
##################################################
# program 1.Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
#
# program 2. Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
####################################################
# #progarm 1
def split_string(n):
    if(len(n)%2 != 0):
        m = n.split(n[int(len(n)/2)])
        m.append(n[int(len(n)/2)])
        print(f'{m[1]}{m[0]}{m[2]}')
    else:
        even = n.split(n[int(len(n)/2)])
        even.append(n[int(len(n)/2)])
        print(f'{even[2]}{even[1]}{even[0]}')

split_string('123456789')


###################################################################
#program 2

def unique_char(n):
    duplicates = 0
    for v in n:
        for i in n:
            if v == i:
                duplicates = duplicates + 1
    print(bool(duplicates == len(n)))

unique_char("tiuoadfgh")