// class Solution {
// public:
//     string removeDuplicates(string s) {
//         vector <char> st;
//         for (char c:s){
//             if ((!st.empty())&&(c==st.back())){
//                 st.pop_back();
//             }
//             else{
//                 st.push_back(c);
                
//             }
//         }
//         s.assign(st.begin(),st.end());
//         return s;
//     }
// };

// more clean version without using vector

class Solution {
public:
    string removeDuplicates(string s) {
        string result;

        for(char c : s) {
            if(!result.empty() && result.back() == c)
                result.pop_back();
            else
                result.push_back(c);
        }

        return result;
    }
};