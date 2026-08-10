class Solution {
    bool flag = true;
    string helper(string word1, string word2){
        if(word1.empty()){
            return word2;
        }else if(word2.empty()){
            return word1;
        }else{
            string ans;
            ans.push_back(flag ? word1[0] : word2[0]);
            flag = !flag;
            ans+=!flag ? helper(word1.substr(1, word1.length()), word2) : helper(word1, word2.substr(1, word2.length()));
            return ans;
        }
    }
public:
    string mergeAlternately(string word1, string word2) {
        flag = true;
        return helper(word1, word2);
    }
};