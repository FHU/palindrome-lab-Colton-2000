#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    flip = word[::-1]
    if word.isalpha() == False:
        return False
    if word == flip:
        return True
    else:
        return False

#YOUR CODE GOES HERE
palindrome(input())