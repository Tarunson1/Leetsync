class Solution {
public:
    int percentageLetter(string s, char letter) {
        int sum = 0;
        // int percent;
        for (char c : s){
        if(c==letter){
            sum++;
        }
        }
        if(!sum) return 0;
        if (!(s.size())) return 0;
        return (sum*100)/s.size();
        //  percent;
    }
};