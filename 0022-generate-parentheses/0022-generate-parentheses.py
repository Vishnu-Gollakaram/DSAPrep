class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def gen_braces(current, op, cl):
            # Base case: if the length of the current list is 2*n, append the pattern as a string
            if len(current) == 2 * n:
                ans.append("".join(current))
                return
            
            # Add an opening parenthesis if we still have available ones
            if op < n:
                current.append("(")
                gen_braces(current, op + 1, cl)
                current.pop()  # Backtrack
            
            # Add a closing parenthesis if the number of closing is less than opening
            if cl < op:
                current.append(")")
                gen_braces(current, op, cl + 1)
                current.pop()  # Backtrack
        
        gen_braces([], 0, 0)
        return ans