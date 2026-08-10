class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> preProduct(nums.size(),0), postProduct(nums.size(),0);
        preProduct[0] = nums[0];
        for(int i = 1; i < nums.size(); ++i){
            preProduct[i] = preProduct[i - 1] * nums[i];
        }
        postProduct[nums.size()-1] = nums[nums.size()-1];
        for(int i = nums.size()-2; i>=0;--i){
            postProduct[i] = postProduct[i+1] * nums[i];
        }

        vector<int> ans(nums.size(),0);
        for(int i = 0; i < nums.size(); ++i){
            if(i == 0){
                ans[i] = postProduct[i + 1];
            }else if(i == nums.size() - 1){
                ans[i] = preProduct[i - 1];
            }else{
                ans[i] = preProduct[i-1] * postProduct[i+1];
            }
        }
        return ans;

    }
};
