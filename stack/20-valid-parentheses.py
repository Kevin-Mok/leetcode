class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s[::-1]:
            if bracket in "([{":
                if len(stack) == 0:
                    return False
                end_bracket = stack.pop()
                if ((bracket == "(" and end_bracket != ")") or
                    (bracket == "[" and end_bracket != "]") or
                    (bracket == "{" and end_bracket != "}")):
                    return False
            else:
                stack.append(bracket)
        if len(stack) > 0:
            return False
        return True

        
if __name__ == "__main__":
    sol = Solution()
    #  base
    #  s = "()[]{}"
    #  r = "aa"
    #  m = "aab"

    #  intertwined
    #  s = "([{}])"

    # wrong
    s = "]"

    print(sol.isValid(s))
