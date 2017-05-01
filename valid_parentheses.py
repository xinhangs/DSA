class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in dict:
                stack.append(char)
            else:
                if len(stack) == 0 or char != dict[stack.pop()]:
                    return False
        else:
            return len(stack) == 0
