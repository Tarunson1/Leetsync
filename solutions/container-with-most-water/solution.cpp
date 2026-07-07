class Solution {
public:
    int maxArea(vector<int>& height) {
        long long hight, area=0;
        int i =0;
        int j = height.size()-1;
        while(i<j){
            hight=min(height[i],height[j]);
            long long area1=hight*(j-i);
            if(area1>=area){
                area=area1;}
                if(hight==height[i]){
                i++;
                }
                else{
                j--;
                }
            
        }
        return area;
        
    }
};