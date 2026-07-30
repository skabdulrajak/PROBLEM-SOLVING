class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]
        
        for word  in words:
            total_weight=0
            for char in word:
                index=ord(char)-ord('a')
                total_weight+=weights[index]
                mod_val=total_weight%26
                char=chr(ord('z')-mod_val)
            res.append(char)
        return "".join(res)
        

