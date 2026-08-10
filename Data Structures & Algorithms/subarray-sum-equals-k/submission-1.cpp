class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int, int> sumCount;
        sumCount[0] = 1;
        int count = 0, sum = 0;
        for(int num : nums){
            sum+=num;
            if(sumCount.find(sum - k) != sumCount.end()){
                count += sumCount[sum - k];
            }
            if(sumCount.find(sum) == sumCount.end()){
                sumCount[sum] = 0;
            }
            sumCount[sum]++;
        }
        return count;
    }
};