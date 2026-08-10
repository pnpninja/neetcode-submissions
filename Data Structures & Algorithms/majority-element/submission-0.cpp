class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }
        int candidate = nums[0], count = 1;
        for(int i = 1; i < nums.size(); ++i){
            count+=(nums[i] == candidate) ? 1 : -1;
            if(count == 0){
                candidate = nums[i];
                count = 1;
            }
        }
        return candidate;
    }
};