class Solution {
    public:
       bool isprime(int n)
        {
            if (n<=1)
            {
                return false;
            }
            if (n<=3)
            {
                return true;
            }
            if (n%2 ==0 || n%3==0)
            {
                return false;
            }
            for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    
    int diagonalPrime(vector<vector<int>>&nums)
    {
        int n=nums.size();
        int maxprime=0;
        for (int i=0;i<n;++i)
        {
            int mainDiag=nums[i][i];
            int antiDiag=nums[i][n-1-i];
            if (mainDiag>maxprime && isprime(mainDiag))
            {
                maxprime =mainDiag;
            }
            if (antiDiag >maxprime &&isprime (antiDiag))
            {
                maxprime=antiDiag;
            }
        }
        return maxprime;
    }
        
        
    
};