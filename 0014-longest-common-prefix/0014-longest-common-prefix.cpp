class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string pre = "";
        if(strs.empty()){
            return "";
        }

        for(int i = 0; i < strs[0].length(); i++){
            char c = strs[0][i];

            for(int j = 1; j < strs.size(); j++){
                if(c != strs[j][i] || i == strs[j].length()){
                    return pre;
                }
            } 
            pre += c;
        }
        return pre;
    }
};