#!/usr/bin/python

def isValid(s):
    stack = []
    ret = True
    for c in s[::-1]:
        if c == ')' or c == ']' or c == '}':
            stack.append(c)
        if c == '(' or c == '[' or c == '{':
            if len(stack) == 0:
                return False
            match = stack.pop()
            if c == '(' and match != ')':
                return False
            if c == '[' and match != ']':
                return False
            if c == '{' and match != '}':
                return False
    
    '''
    栈内没有元素。说明全部被匹配到了，否则说明还有括号未匹配
    '''
    if len(stack) != 0:
        return False

    return ret


print isValid("{}")
print isValid("[[]]")
print isValid("[[}]")
print isValid("")
