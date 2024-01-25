class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        for (int i = 1; i < prices.size(); i += 1) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};