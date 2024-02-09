#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    flip = word[::-1]
    if word == flip:
        palindrome = True
    elif word.isalpha() == False:
        palindrome = False
    else:
        palindrome = False
    return palindrome

#YOUR CODE GOES HERE
word = input()
palindrome(word)

#comment to resubmit