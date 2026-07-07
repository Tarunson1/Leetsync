// class Solution {
// public:
//     vector<int> getBiggestThree(vector<vector<int>>& grid) {
//         int row = grid.size(); //for extracting row
//         int col = grid[0].size();
//         set <int> st;

//         vector <vector<int> d1 (m,vector<int>(n,0));
//         vector <vector<int> d2 (m,vector<int>(n,0));
//         auto addSet = [&] (int sum){ // here & make the lambda funciton to
//         acces all values inside the class we dont need to make it ouotside
//         the class and auto is used to declare the lambda function
//                     st.insert(sum);
//                     if(st.size()>3){
//                         st.erase(begin(st)); //making set to constent size to
//                         store only top 3 values
//         }
//                 };

//         // precalculating the diagonal sum fro optimized version

//         for(int i = 0 ; i<row;i++){
//             for (int j = 0 ; j<col;j++){

//                 // for 0 th radius rhombus
//                     addSet(grid[i][j]);

//                 for (int side = 1; i-side>=0 && i+side <row && j-side>=0 &&
//                 j+side<col;side++){
//                     int sum=0;
//                     //side is the radius of the rhombus
//                     for(int k = 0 ; k<=side-1;k++){

//                     sum += grid[i-side+k][j+k]; //here k = 0 pr corner ban
//                     jayega then k=1 pr diagonally top to right jayegaa sum +=
//                     grid[i+k][j+side-k]; //right to bottem

//                     sum += grid[i+side-k][j-k]; //bottem to left

//                     sum+= grid[i-k][j-side+k]; //left to top
//                     }
//                     addSet(sum);

//                 }
//             }
//         }
//         return vector<int>(rbegin(st),rend(st)); //return using rbegin that
//         start from last in ordered set which is sorted
//     }
// };

class Solution {
public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int row = grid.size(); // for extracting row
        int col = grid[0].size();
        set<int> st;

        vector<vector<int>> d1(row, vector<int>(col, 0));
        vector<vector<int>> d2(row, vector<int>(col, 0));
        auto addSet = [&](int sum) { // here & make the lambda funciton to acces
                                     // all values inside the class we dont need
                                     // to make it ouotside the class and auto
                                     // is used to declare the lambda function
            st.insert(sum);
            if (st.size() > 3) {
                st.erase(begin(st)); // making set to constent size to store
                                     // only top 3 values
            }
        };

        // precalculating the diagonal sum fro optimized version
        // build diagonals
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                d1[i][j] = grid[i][j];
                if (i - 1 >= 0 && j - 1 >= 0)
                    d1[i][j] += d1[i - 1][j - 1];

                d2[i][j] = grid[i][j];
                if (i - 1 >= 0 && j + 1 < col)
                    d2[i][j] += d2[i - 1][j + 1];
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                // for 0 th radius rhombus
                addSet(grid[i][j]);

                for (int side = 1; i - side >= 0 && i + side < row &&
                                   j - side >= 0 && j + side < col;
                     side++) {
                    int top_i = i - side, top_j = j;
                    int right_i = i, right_j = j + side;
                    int bottom_i = i + side, bottom_j = j;
                    int left_i = i, left_j = j - side;
                    int sum = 0;
                    // top to right edge

                    // top → right (↘ using d1)
                    sum += d1[right_i][right_j];
                    if (top_i - 1 >= 0 && top_j - 1 >= 0)
                        sum -= d1[top_i - 1][top_j - 1];

                    // right → bottom (↙ using d2)
                    sum += d2[bottom_i][bottom_j];
                    if (right_i - 1 >= 0 && right_j + 1 < col)
                        sum -= d2[right_i - 1][right_j + 1];

                    // bottom → left (↘ using d1)
                    sum += d1[bottom_i][bottom_j];
                    if (left_i - 1 >= 0 && left_j - 1 >= 0)
                        sum -= d1[left_i - 1][left_j - 1];

                    // left → top (↙ using d2)
                    sum += d2[left_i][left_j];
                    if (top_i - 1 >= 0 && top_j + 1 < col)
                        sum -= d2[top_i - 1][top_j + 1];

                    // REMOVING THE DOUBLE COUNTING OF THE CORNERS
                    sum -= grid[top_i][top_j];
                    sum -= grid[right_i][right_j];
                    sum -= grid[bottom_i][bottom_j];
                    sum -= grid[left_i][left_j];
                    addSet(sum);
                }
            }
        }
        return vector<int>(rbegin(st),
                           rend(st)); // return using rbegin that start from
                                      // last in ordered set which is sorted
    }
};