class Solution {
public:
    int minimizedStringLength(string s) {
        // vector <char> v;
        // for (char c: s){
        //     if (!v.empty() && v.back() == c){
        //         v.pop_back();
        //            v.push_back(c);
        //     }
        //     else{
        //         v.push_back(c);
        //     }
        // }
        // return v.size();

        // usefull when i have to remove adjacent element not the whole duplication 

        // use unordered set for this it will be more efficient then the stack 
        unordered_set <char> st;
        for (char c:s){
            st.insert(c);
        }
        return st.size();
    }
};