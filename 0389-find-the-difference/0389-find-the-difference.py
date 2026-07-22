class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list = list(t)

        for ch in s:
            t_list.remove(ch)

        return t_list[0]
