class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector <pair<char,int>> v;
        for (char ele: s){
            if (v.empty()){
                v.push_back({ele,1});
            }
            else if (v.back().first==ele){
                v.back().second++;
            if (v.back().second==k){
                v.pop_back();
            }
            }
            else{
                v.push_back({ele,1});
            }
        } 
        string g;
        for (auto &p:v){
            g.append(string(p.second,p.first));
        }
        return g;
    }
};