class Solution {
    int partition(vector<int>& nums, int left, int right, int partitionIndex){
        swap(nums[partitionIndex], nums[right]);
        int pivot = nums[right];
        int i = left;
        for(int j = left; j < right; ++j){
            int couldBeSame = rand() % 2;
            if((couldBeSame && nums[j] <= pivot) || (!couldBeSame && nums[j] < pivot)){
                swap(nums[i], nums[j]);
                ++i;
            }
        }
        swap(nums[i], nums[right]);
        return i;
    }

    void quickSort(vector<int>& nums, int left, int right){
        if(left >= right) return;
        int partitionIndex = (left + right) / 2;
        int movedPartitionIndex = partition(nums, left, right, partitionIndex);
        quickSort(nums, left, movedPartitionIndex - 1);
        quickSort(nums, movedPartitionIndex + 1, right);
        return;
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        quickSort(nums, left, right);
        return nums;
    }
};