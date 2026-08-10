class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int leftPtr = 0, rightPtr = 0;
        int numsSize = nums.size();
        while(rightPtr < numsSize){
            if(nums[rightPtr] != val){
                nums[leftPtr] = nums[rightPtr];
                rightPtr++;
                leftPtr++;
            }else{
                rightPtr++;
            }
        }
        return leftPtr;
    }
};