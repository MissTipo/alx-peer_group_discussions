'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{)"    stack -> [(, ]
Output: true

Example 3:

Input: s = "(]"  '{}())'
Output: false

pseudocode:
    def isValid(self, s: str) -> bool:
        if len(s) is odd:
            return False

        stack = []

        create a dictionary of available pairs

        pair = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
        }
        
        for c in s:
            if c in pair:
                stack.append(c) [ { ]
            
            else:
                val = stack.pop()
                if pair[val] != c:
                    return False

        if len(stack) == 0:
            return True
    
'''


def isValid(s: str) -> bool:
    if len(s) % 2:
        return False

    stack = []

    # create a dictionary of available pairs

    pair = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for c in s:
        if c in pair:
            stack.append(c)  # [ { ]

        else:
            val = stack.pop()
            if pair[val] != c:
                return False

    if len(stack) == 0:
        return True

    return False


# Testing
s = "()[]{)"
print(isValid(s))
print()

s = '({[]})'
print(isValid(s))
print()

s = '{}[]()'
print(isValid(s))
