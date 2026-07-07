class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m1{};
        for (int i=0;i<nums.size();i++){
            int more=target-nums[i];
            if(m1.find(more)!=m1.end()){
                return {m1[more],i};
            }
            m1[nums[i]]=i;
        }
        return {};
    }
};