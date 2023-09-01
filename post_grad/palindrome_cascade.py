'''A palindrome is a word, sentence, verse or number that reads the same backwards or forward. 
A typical palindrome class will accept a parameter such as a word or number and return true or false if the word is a palindrome.
However, your task is to implement a cascading palindrome - a cascading palindrome in the context of this task means the following:

1. The class takes a parameter with several components. 
    The parameter could be a word, a sentence, multiple numbers, etc. 
    The parameter contains various items separated by space. 
2. The class determines the part of the parameter that is a palindrome and returns only 
    the palindrome part of the parameter.
    For clarity, consider these examples:

a. 1230321  returns 1230321
b. 1230321 09234 0124210 returns 1230321 0124210
c. abcd5dcba 1230321 09234 0124210 returns abcd5dcba 1230321 0124210

You can assume that the example structure above will always be the case for this task. 
For example, this sentence: "A man, a plan, a canal – Panama" is a palindrome; however, 
you don't need to consider such a case in your implementation.

While implementing a palindrome or even a cascading palindrome could be considered easy, the difficulty is efficiency. Your code needs to consider the following:

1. Efficiency: Use as little memory as possible
2. Speed: Ensure the fastest result regardless of how many components the parameter has
3. Validation: validation data given by users and return appropriate responses if invalid data is given
4. Error handling: return appropriate error messages when something goes wrong.
 
Hint:
    You'll see that for each word above, that is a palindrome.
    The letter in the centre forms the base of your check. If the letters on the right and 
    to the left of the centre letter are not the same,
    then such a word is not a palindrome, and you'll not need to do any further checks. 
'''


class Palindrome:
    '''Cascading palindrome implementation'''

    def __init__(self, param):
        '''Initialize class'''
        self.param = param

    # if odd, keep mid and compare left to right
    # if even, compare one half to the other # no|on

    def ispal(self, word):
        '''returns True if a word is palindrome, else False'''
        l = len(word)
        if l % 2 == 0:
            m = l // 2
            if word[:m] == word[-1:(m - 1):-1]:
                return True

        else:
            m = l // 2
            if word[:m] == word[-1:m:-1]:
                return True

        return False

    def casc_palindrome(self):
        '''returns cascading palindrome'''
        res = []
        for word in self.param.split():
            if self.ispal(word):
                res.append(word)

        return ' '.join(res)


a = '1230321'  # returns 1230321
b = '1230321 09234 0124210'  # returns 1230321 0124210
c = 'abcd5dcba 1230321 09234 0124210'  # returns abcd5dcba 1230321 0124210

p1 = Palindrome(a)
print(p1.casc_palindrome() == a)
print()
p2 = Palindrome(b)
print(p2.casc_palindrome())
print()
p3 = Palindrome(c)
print(p3.casc_palindrome())
