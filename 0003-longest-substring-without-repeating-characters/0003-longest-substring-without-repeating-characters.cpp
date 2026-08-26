class Solution {
public:
    int lengthOfLongestSubstring(string s) {

       std::vector<int> last_seen(256,-1);

       int max = 0;
       int left = 0;

       for(int right=0; right<s.length(); right++){
        char curr = s[right];

        if(last_seen[curr] >= left){
            left = last_seen[curr] + 1;
        }

        last_seen[curr] = right;

        max = std::max(max, right - left + 1);
       }

       return max;
    }
};