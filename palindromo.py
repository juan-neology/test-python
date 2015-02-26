__author__ = 'juan'

def palindrome(word):
    x = 0
    for i in range (len(word)/2):
        if (word[x]) == (word[len(word)-x-1]):
            x+=1
        if x == (len(word)/2):
            return True
    return False

print palindrome('noneenon')
