class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
    //     vector<int> ans;
    //     ans.push_back(left + 1);
    //     ans.push_back(right + 1);
    //     return ans;
    // }
    // this is equivalant to -------------
    // return {left+1,right+1};

    int left = 0 ;
    int right = numbers.size()-1;
    int sum = 0;
    while(left<right){
        sum = numbers[left]+numbers[right];
        if(sum==target){
            return{left+1,right+1};

        }
        else if(sum>target){
            right--;
        }
        else if(sum<target){
            left++;
        }
    }
        return {};
    }
};