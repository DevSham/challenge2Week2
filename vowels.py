
#creating a variable to hold the sentence entered by the user.
list_string = input("please enter a sentence of your choice.").lower().split(' ')# split is to remove spaces between words.
#creating an empty string.
empty_string = " "
#adding user characters to empty string.
for characters in list_string:
        empty_string += characters
#creating a list of vowels.
vowels = ["a", "e", "i", "o", "u"]
#creating a list to hold vowels in the string(empty_string) entered by the user.
vowels_in_string = [vowel for vowel in vowels if vowel in empty_string]
#creating an empty string that is going to hold the vowwels present in the user's string and s
vowels_string  = ""
for vowel in vowels_in_string:
        vowels_string += vowel
#empty list to hold letters that appear more than once
duplicates = []
dup = [duplicates.append(character) for character in empty_string if empty_string.count(character) > 1 and character not in duplicates]
print(duplicates)
answer = (vowels_string, len(duplicates))
print(answer)



