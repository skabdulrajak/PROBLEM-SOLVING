class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        cz_count = 0  
        mz_count = 0
        co_count = 0  
        mo_count = 0
        
        for i in s:
            if i == '1':
                co_count += 1
                cz_count = 0
                mo_count = max(co_count, mo_count)
            elif i == '0':
                cz_count += 1
                co_count = 0  
                mz_count = max(cz_count, mz_count)
        
        return mo_count > mz_count