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
        
		return len(stack) == 0
	
    def isValid1(self, s):
        """
        Extension: only ( and ) with constant extra space.
		Test case: ['', '(', ')', '())', '(()', '(()))', '((())', '())(()']
        """
		counter = 0
        for char in s:
            if char == '(':
				counter += 1
			elif char == ')':
				if counter == 0:
					return False
				counter -= 1
				
		return counter == 0
