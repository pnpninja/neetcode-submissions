class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> numToLoc;
        for(int i = 0; i < nums.size(); ++i){
            int diff = target - nums[i];
            if(numToLoc.find(diff) != numToLoc.end()){
                return {numToLoc[diff], i};
            }
            if(numToLoc.find(nums[i]) == numToLoc.end()){
                numToLoc[nums[i]] = i;
            }
        }
        return {-1, -1};
    }
};
