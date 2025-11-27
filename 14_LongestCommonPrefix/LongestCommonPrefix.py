from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs is None:
            return ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(len(strs)):
                if (i == len(strs[j]) or strs[j][i] != ch):
                    return strs[0][:i]
        return strs[0]