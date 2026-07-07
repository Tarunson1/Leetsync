// #include <vector>
// #include <set>
// using namespace std;

// class Solution {
// public:
//     set<int> temp;
//     vector<int> ar = vector<int>(101, 0);

//     void unique(vector<int>& num){
//         for (int i : num){
//             temp.insert(i);
//         }
//     }

//     void count(set<int> &s){
//         for (int j : s){
//             ar[j]++;
//         }
//     }

//     void res(vector<int>& result){
//         for(int k = 1; k <= 100; k++){
//             if(ar[k] >= 2){
//                 result.push_back(k);
//             }
//         }
//     }

//     vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {

//         vector<int> result;

//         unique(nums1);
//         count(temp);
//         temp.clear();

//         unique(nums2);
//         count(temp);
//         temp.clear();

//         unique(nums3);
//         count(temp);

//         res(result);

//         return result;
//     }
// };
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {

        int mask[101] = {0};

        for(int x : nums1) mask[x] |= 1;
        for(int x : nums2) mask[x] |= 2;
        for(int x : nums3) mask[x] |= 4;

        vector<int> result;

        for(int i = 1; i <= 100; i++){
            if(__builtin_popcount(mask[i]) >= 2){
                result.push_back(i);
            }
        }

        return result;
    }
};