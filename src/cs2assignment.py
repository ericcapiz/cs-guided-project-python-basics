# Given a string, return a new string with all the vowels removed.

# Examples:

# csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

def csRemoveTheVowels(input_str):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for char in input_str:
        if char in vowels:
            input_str = input_str.replace(char, "")
    return(input_str)

#######################################################

# Given a string of words, return the length of the shortest word(s).

# Notes:

# The input string will never be empty 
# and you do not need to validate for different data types.

def csShortestWord(input_str):
    new_str = input_str.split()
    word = min(new_str, key=len)
    return(len(word))

#####################################################################

# Given an array of integers, return the sum of all the positive integers in the array.

# Examples:

# csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
# csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
# csSumOfPositive([-3, -2]) -> 0
# Notes:

#If the input_arr 
# does not 
# contain any 
# positive integers, the default sum should be 0.

def csSumOfPositive(input_arr):
    new_list = [num for num in input_arr if num > 0]
    total = 0
    for num in new_list:
        total+= num
    print(new_list)
    print(total)
    return(total)

########################################################################

# Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

# Examples:

# csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
# csLongestPossible("abc", "abc") -> "abc"

def csLongestPossible(str_1, str_2):
    new_str = str_1 + str_2
    print(new_str)
    print("".join(dict.fromkeys(str_1)))
    print("".join(dict.fromkeys(str_2)))
    final_str = "".join(dict.fromkeys(new_str))
    print(final_str)
    return(''.join(sorted(final_str)))

########################################################################################

# Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

# Examples:

# csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
# csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
# csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
# Notes:

# The output can contain the digit 5.
# The start number will always be less than the end number (both numbers can also be negative).

def csAnythingButFive(start, end):
    total = 0
    for num in range(start,end +1 ,+1):
        if '5' in str(num):
            print("false")
        else:
            total += 1
            print("true")
        print(total)
    return(total)