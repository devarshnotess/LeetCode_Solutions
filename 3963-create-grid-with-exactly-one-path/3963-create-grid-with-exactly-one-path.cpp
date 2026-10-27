class Solution {
public:
    vector<string> createGrid(int m, int n){

        /// THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        /// explanatory comments are included for readability and future reference's as well

        /// we just want to return a grid where a valid exactly one path exists hence we first go right up till n turns and then we just go down uptill the end of the limit of m the whole configuration results in valid one path
        vector<string> grid(m);
        grid[0] = string(n, '.');
        string row = string(n - 1, '#') + '.';
        for(int i = 1; i < m; i++){
            grid[i] = row;
        }
        return grid; /// final grid
    }
};