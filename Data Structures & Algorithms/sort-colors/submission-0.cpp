class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Move zeroes to left
        int numsSize = nums.size();
        int left = 0, right = 0;
        while(right < numsSize){
            if(nums[right] == 0){
                swap(nums[left], nums[right]);
                left++;
                right++;
            }else{
                right++;
            }
        }

        // Move 2s to right
        left = numsSize - 1, right = numsSize - 1;
        while(left >= 0){
            if(nums[left] == 2){
                swap(nums[left], nums[right]);
                left--;
                right--;
            }else{
                left--;
            }
        }
    }
};