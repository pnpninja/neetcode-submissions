class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> unique_nums;
        int longestSeq = 0;
        for(int num : nums){
            unique_nums.insert(num);
        }
        for (int num : unique_nums){
            if(unique_nums.find(num - 1) == unique_nums.end()){
                int curSize = 1, curNum = num;
                while(unique_nums.find(curNum + 1) != unique_nums.end()){
                    curSize++;
                    curNum++;
                }
                longestSeq = max(longestSeq, curSize);
            }
        }
        return longestSeq;
    }
};
