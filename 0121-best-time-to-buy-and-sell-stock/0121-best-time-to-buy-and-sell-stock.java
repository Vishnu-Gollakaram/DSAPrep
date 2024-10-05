class Solution {
    public int maxProfit(int[] prices) {
        // maximum profit is 0
        // minimum is taken as inf
        int maxProfit = 0;
        int minimumEle = 10000;
        
        // for each price in prices
        for (int price: prices) {
            // if price < min min = price
            if (price < minimumEle) {
                minimumEle = price;
            }
            int estProf = price - minimumEle;
            // if prof > maxProf maxProf = estProf
            if (maxProfit < estProf) {
                maxProfit = estProf;
            }
        }
        return maxProfit;
    }
}