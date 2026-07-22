class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()

        if len(pattern) != len(ss):
            return False

        zip_set = set(zip(pattern, ss))

        return len(zip_set) == len(set(pattern)) == len(set(ss))