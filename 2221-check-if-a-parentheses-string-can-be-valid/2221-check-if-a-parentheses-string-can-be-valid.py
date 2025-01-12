class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        if n % 2 == 1:
            return False

        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False 

        brackets = []
        arr = []

        for i in range(n):
            if locked[i] == "0":
                arr.append(i)
            elif s[i] == "(":
                brackets.append(i)
            else:
                if brackets:
                    brackets.pop()
                elif arr:
                    arr.pop()
                else:
                    return False
        
        while brackets and arr and brackets[-1] < arr[-1]:
            brackets.pop()
            arr.pop()

        if brackets:
            return False
        
        return True