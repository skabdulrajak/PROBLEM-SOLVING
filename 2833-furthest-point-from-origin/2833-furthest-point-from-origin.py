class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        b=0
        for i in moves:
               if i=="L":
                l=l-1
               elif i=="R":
                r+=1
               else:
                b+=1
        return abs(l+r)+b