class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int len = -1;
        int shortestLen = INT_MAX;
        for(const auto& str : strs){
            shortestLen = min(shortestLen, (int)str.size());
        }
        if(shortestLen == 0){
            return "";
        }

        bool terminationCondition = false;
        for(int i = 0; i < shortestLen; ++i){
            char ltr = strs[0][i];
            for(int j = 1; j < strs.size(); ++j){
                if(strs[j][i] != ltr){
                    terminationCondition = true;
                    break;
                }
            }
            if(terminationCondition){
                if(len == -1){
                    return "";
                }else{
                    return strs[0].substr(0, i);
                }
            }else{
                len = i;
            }
        }
        return strs[0].substr(0, shortestLen);
    }
};