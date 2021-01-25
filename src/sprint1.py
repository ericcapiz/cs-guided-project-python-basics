# Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

# Examples:

# csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
# csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]

def csReverseString(chars):
    return chars[::-1]



#############################################

# A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

# Given a string, write a function that checks if the input is a valid palindrome.

# Examples:

# csCheckPalindrome("racecar") -> true
# csCheckPalindrome("anna") -> true
# csCheckPalindrome("12345") -> false
# csCheckPalindrome("12321") -> true

def csCheckPalindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False
    
    ######################################
    
    # Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.


def csRemoveDuplicateWords(input_str):
    words = input_str.split()
    return (" ".join(sorted(set(words), key=words.index)))