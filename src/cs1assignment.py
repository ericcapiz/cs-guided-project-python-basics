#Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

def csWhereIsBob(names):
    find_bob = "Bob"
    if find_bob in names:
        index = names.index(find_bob)
        return index
    else:
        return -1
    
    ########################################################################################################################
    
#Create a function that returns True if the given string has any of the following:

# Only letters and no numbers.
# Only numbers and no letters.
# If a string has both numbers and letters or contains characters that don't fit into any category, return False.

def csAlphanumericRestriction(input_str):
    if input_str.isalpha():
        return True
    elif input_str.isdigit():
        return True
    else:
        return False


##########################################################################################################################################


# Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

# Examples:

# csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
# csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"

def csOppositeReverse(txt):
    flipped = txt[::-1]
    print(flipped.swapcase())
    return(flipped.swapcase())


#######################################################################################

# Create a function that given an integer, returns an integer where every digit in the input integer is squared.

# Examples:

# csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
# csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9

def csSquareAllDigits(n):
    number = str(n)
    new_number = ''
    for num in number:
        new_number = new_number + str(int(num)**2)
    return int(new_number)


#######################################################################################



# Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

# Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

# Examples:

# csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"

def csSchoolYearsAndGroups(years, groups):
    result = ''
    print ("Initial list : " + str(result))
    alpha = 'a'
    for year in range(1, years + 1):
        alpha = 'a'
        for group in range(1, groups + 1 ):
            result += (str(year) + alpha + ', ')
            alpha = chr(ord(alpha) +1)
    return ( str(result)[:-2])


#######################################################################################


    
    
#     Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends with a 7, ignore that chord.

# Examples:

# csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
# csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
# csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]

def csMakeItJazzy(chords):
    my_list = []
    new_chord = ''
    for chord in chords:
        if chord[-1] == '7':
            new_chord = chord
            my_list.append(new_chord)
        else:
            new_chord = chord + '7'
            my_list.append(new_chord)
        print(new_chord)
    return(my_list)

######test