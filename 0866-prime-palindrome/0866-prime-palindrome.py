class Solution:
    def isPrime(self, num):
        if num == 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    
    def makePalindrome(self, num):
        s = str(num)
        ans = s + s[:-1][::-1]
        return int(ans)
    
    def primePalindrome(self, n):
        if n <= 2: return 2
        elif n <= 3: return 3
        elif n <= 5: return 5
        elif n <= 7: return 7
        elif n <= 11: return 11
        
        i = 1
        while True:
            palin = self.makePalindrome(i)
            if palin >= n and self.isPrime(palin):
                return palin
            i += 1