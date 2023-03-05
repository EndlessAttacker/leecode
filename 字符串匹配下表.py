class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

            return haystack.index(needle) if needle in haystack else -1


s = Solution()
haystack = "sadbutsad"
needle = "sado"
print(s.strStr(haystack,needle))