class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        int n = nums.size();
        if(n <= 3) return 0;
        sort(nums.begin(), nums.end());
        int lower = 0; // always 0, can be shown zero
        int high = min({nums[n - 1] - nums[2], 
                        nums[n - 3] - nums[0],
                        nums[n - 2] - nums[1]});
        return lower + high;
    }
};