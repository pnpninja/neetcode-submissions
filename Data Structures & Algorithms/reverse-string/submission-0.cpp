class Solution {
public:
    void reverseString(vector<char>& s) {
        int sLen = s.size();
        int left = 0, right = sLen - 1;
        while(left < right){
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }
};