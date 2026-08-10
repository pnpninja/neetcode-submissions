class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> numsNonDup;
        for(int num : nums){
            if(numsNonDup.find(num) != numsNonDup.end()){
                return true;
            }
            numsNonDup.insert(num);
        }
        return false;
    }
};