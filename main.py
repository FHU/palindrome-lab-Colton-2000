#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    if word == '':
        return False
    word = word.replace(' ','')
    word = word.lower()
    flip = word[::-1]
    if word.isalpha() == False:
        return False
    else:
        return word == flip

#YOUR CODE GOES HERE
palindrome(input())