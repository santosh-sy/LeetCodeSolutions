class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif len(haystack) < len(needle):
            return -1
        else:
            hayLength = len(haystack)
            needleLength = len(needle)

            for i in range((hayLength - needleLength) + 1):
                if haystack[i:i + needleLength] == needle:
                    return i
            return -1