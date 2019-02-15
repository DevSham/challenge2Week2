#pythoonfunction to return fizz if combined length of strings is divisible by 3,
#Buzz if it is divisible by 5 and fizzBuzz if it is divisible by both 5 and 3.
def Fizzbuzz(list1, list2):
# getting the length of the strings.
    x = len(list1)
    y = len(list2)
# adding string lengths.
    z = x+y
# checking if the combined lengths is divisible 3. 
    if z%3 == 0:
        return "Fizz"
# checking if combined length is divisible by 5.
    elif z%5 == 0:
        return "Buzz"
    else:
# checking if combined length is divisible by both 5 and 3.
        if z%5 == 0 and z%3 == 0:
            return "Fizzbuzz"
#calling the function
print(Fizzbuzz([1, 2, 3], [1, 2]))
