class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int uniqueIndex = 0, iter = 1;
        int len = nums.size();
        while(iter < len){
            if(nums[iter] == nums[uniqueIndex]){
                iter++;
            }else{
                nums[uniqueIndex+1] = nums[iter];
                uniqueIndex++;
                iter++;
            }
        }
        return uniqueIndex + 1;
    }
};