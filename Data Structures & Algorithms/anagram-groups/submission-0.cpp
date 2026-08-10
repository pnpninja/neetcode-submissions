class Solution {
private:
    string generateSignature(const string& str){
        vector<int> count(26,0);
        for(char c : str){
            count[c-'a']++;
        }
        string ans;
        for(int i = 0; i < 26; ++i){
            ans+=(char)(i + 'a');
            ans+=to_string(count[i]);
        }
        return ans;
    }
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> hashmap;
        for(const string& str: strs){
            string signature = generateSignature(str);
            hashmap[signature].push_back(str);
        }
        vector<vector<string>> answer;
        for(const auto& [key, value]: hashmap){
            answer.push_back(value);
        }
        return answer;
    }
};
