class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int nums1Ptr = m - 1, nums2Ptr = n - 1;
        int combinedPtr = m + n - 1;
        while(nums1Ptr >= 0 && nums2Ptr >= 0){
            if(nums1[nums1Ptr] > nums2[nums2Ptr]){
                nums1[combinedPtr] = nums1[nums1Ptr];
                combinedPtr--;
                nums1Ptr--;
            }else{
                nums1[combinedPtr] = nums2[nums2Ptr];
                combinedPtr--;
                nums2Ptr--;
            }
        }
        if(nums1Ptr < 0){
            while(nums2Ptr >= 0){
                nums1[combinedPtr] = nums2[nums2Ptr];
                combinedPtr--;
                nums2Ptr--;
            }
        }else if(nums2Ptr < 0){
            while(nums1Ptr >= 0){
                nums1[combinedPtr] = nums1[nums1Ptr];
                combinedPtr--;
                nums1Ptr--;
            }
        }
    }
};