class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max=0
        for i in range (len(arr)):
            if arr[i]>max:
                max=arr[i]
                index=i
        return index

