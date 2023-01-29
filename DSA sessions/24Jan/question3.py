"""
Leetcode 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
"""


################################
""" Post Interview Solution """
################################

def isValidParenthesis(s: str) -> bool:
        para = []   #stack to check previous parenthesis
        if len(s)&1 == 1 : return False
        for k in s :
            if k == '(' or k == '{' or  k == '[':
                para.append(k)
            else :
                if len(para)==0 or (k == ')' and para[-1] != '(') or (k == '}' and para[-1] != '{') or (k == ']' and  para[-1] != '[') :
                    return False
                para = para[:-1]
        if len(para) > 0 : return False

        return True
