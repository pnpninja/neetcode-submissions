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
        //return helper(word1, word2);
        int ptr1 = 0, ptr2 = 0;
        string ans;
        while(ptr1 < word1.length() && ptr2 < word2.length()){
            ans+=word1[ptr1];
            ans+=word2[ptr2];
            ptr1++;
            ptr2++;
        }
        if(ptr1 == word1.length()){
            ans+=word2.substr(ptr2, word2.length() - ptr2);
        }else if(ptr2 == word2.length()){
            ans+=word1.substr(ptr1, word1.length() - ptr1);
        }
        return ans;
    }
};