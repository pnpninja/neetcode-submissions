class Solution {
public:
        vector<int> majorityElement(vector<int>& nums) {
        int* candidate1 = NULL;
        int* candidate2 = NULL;
        int count1 = 0, count2 = 0;
        for(int num : nums){
            if(candidate1 != NULL && *candidate1 == num){
                count1++;
            }else if(candidate2 != NULL && *candidate2 == num){
                count2++;
            }else if(count1 == 0){
                candidate1 = new int(num);
                count1 = 1;
            }else if(count2 == 0){
                candidate2 = new int(num);
                count2 = 1;
            }else{
                count1--;
                count2--;
            }
        }

        count1 = 0, count2 = 0;
        for (int n: nums) {
            if (candidate1 != NULL && n == *candidate1) count1++;
            if (candidate2 != NULL && n == *candidate2) count2++;
        }

        int n = nums.size();
        vector<int> result;
        if (candidate1 != NULL && count1 > n/3) result.push_back(*candidate1);
        if (candidate2 != NULL && count2 > n/3) result.push_back(*candidate2);

        return result;
    }
};