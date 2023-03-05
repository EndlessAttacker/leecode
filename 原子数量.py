import re
import collections
class Solution(object):
    def countOfAtoms(self, formula: str) -> str:

        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)",formula)

        stack = [collections.Counter()]
        for name,m1,left,right,m2 in parse:
            if name:
                stack[-1][name] = int(m1 or 1)

            if left:
                stack.append(collections.Counter())
            if right:
                top = stack.pop()
                for i in top:
                    stack[-1][i] += top[i] * int(m2 or 1)
        return "".join (name+(str(stack[-1][name])if stack[-1][name] > 0 else "") for name in sorted(stack[-1]))
if __name__=='__main__':
    solution = Solution()
    inp = "H2O"
    so = solution.countOfAtoms(inp)
    print(so)
    
