static const int _ = [](){ios_base::sync_with_stdio(false);cin.tie(NULL);return 0;}();

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        for (int i = 0; i < (1 << n); ++i)
            result.push_back(i ^ (i >> 1));
        return result;
    }
};