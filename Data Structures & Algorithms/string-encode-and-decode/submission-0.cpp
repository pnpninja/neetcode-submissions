class Solution {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encodedString;
        for(string s : strs){
            for(char c : s){
                if(c == '/'){
                    encodedString+='/';
                }
                encodedString+=c;
            }
            encodedString+="/:";
        }
        return encodedString;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> originalStrings;
        string str;
        int index = 0;
        while(true){
            if(index == s.size()){
                break;
            }
            if(index < s.size() - 1 && s[index] == '/'){
                if(s[index + 1] == '/'){
                    str+='/';
                    index+=2;
                }else if(s[index + 1] == ':'){
                    originalStrings.push_back(str);
                    str.clear();
                    index+=2;
                }
            }else{
                str.push_back(s[index]);
                index++;
            }
        }
        return originalStrings;
    }
};
