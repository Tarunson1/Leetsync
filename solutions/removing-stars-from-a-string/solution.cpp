class Solution {
public:
    string removeStars(string s) {
        vector<char> v;
        for (char ele:s){
            if(v.empty()&&ele=='*'){
                continue;
            }
            else if(ele=='*'){
                v.pop_back();
            }
            else{
                v.push_back(ele);
            }
        }
        string g;
        for (char i : v){
            g+=i;
        }
        return g;
    }
};