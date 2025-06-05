class Solution {
public:

    int numIdenticalPairs(vector<int>& nums) {
        map<int, int> mp;
        int sum(0);
        for(int i : nums) {
            mp[i] ++;
        }

        for (std::map<int, int>::iterator it = mp.begin(); it != mp.end(); ++it) {
           if(it->second>1) {
            int n = it->second;
            sum += (n*(n-1)/2);
           }
       }

       return sum;

    }
};