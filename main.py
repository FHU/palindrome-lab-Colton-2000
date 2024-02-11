#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    flip = word[::-1]
    if word.isalpha() == False:
        palindrome = False
    elif word == flip:
        palindrome = True
    else:
        palindrome = False
    return palindrome

#YOUR CODE GOES HERE
word = input()
palindrome(word)