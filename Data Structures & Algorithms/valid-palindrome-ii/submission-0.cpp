class Solution {
    bool isPalindromeHelper(string& s, int i, int j){
        while(i <= j){
            if(s[i]!=s[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
public:
    bool validPalindrome(string s) {
        int left = 0, right = s.length() -1;
        while(left < right){
            if(s[left] != s[right]){
                return isPalindromeHelper(s, left + 1, right) || isPalindromeHelper(s, left, right - 1);
            }
            left++;
            right--;
        }
        return true;
    }
};