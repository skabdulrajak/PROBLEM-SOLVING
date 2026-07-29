class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        for row in matrix:
            degree=sum(row)
            ans.append(degree)
        return ans