#creating a function that returns a string of vowels and the number
#  of letters that appear more than once in a sentence.
def vowel(list_string1):
        #creating a variable to hold the sentence entered by the user.
        list_string = list_string1.lower().split(' ')# split is to remove spaces between words.
        #creating an empty string that will hold characters entered by user.
        empty_string = " "
        #adding user characters to empty string.
        for characters in list_string:
                empty_string += characters
        #creating a list of vowels.
        vowels = ["a", "e", "i", "o", "u"]
        #creating a list to hold vowels in the string(empty_string) entered by the user.
        vowels_in_string = [vowel for vowel in vowels if vowel in empty_string]
        #creating an empty string that is going to hold the vowwels present in the user's string.
        vowels_string  = ""
        for vowel in vowels_in_string:
                vowels_string += vowel
        #empty list to hold letters that appear more than once and not repeated
        duplicates = []
        dup = [duplicates.append(character) for character in empty_string if empty_string.count(character) > 1 and character not in duplicates]
        #returning the number of duplicates and the vowels in the sentence.
        answer = (vowels_string, len(duplicates))
        return answer
print(vowel("please enter a sentence of your choice."))



