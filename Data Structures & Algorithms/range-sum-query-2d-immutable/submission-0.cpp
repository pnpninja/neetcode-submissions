class NumMatrix {
    vector<vector<int>> matrixSum;
public:
    NumMatrix(vector<vector<int>>& matrix) {

        // Calculate rowSum
        int rows = matrix.size(), cols = matrix[0].size();
        vector<vector<int>> rowSum(rows, vector<int>(cols));
        vector<vector<int>> columnSum(rows, vector<int>(cols));
        matrixSum = vector<vector<int>>(rows, vector<int>(cols));
        for(int row = 0; row < rows; ++row){
            rowSum[row][0] = matrix[row][0];
            for(int col = 1; col < cols; ++col){
                rowSum[row][col] = rowSum[row][col - 1] + matrix[row][col];
            }
        }

        // Calculate columnSum
        for(int col = 0; col < cols; ++col){
            columnSum[0][col] = matrix[0][col];
            for(int row = 1; row < rows; ++row){
                columnSum[row][col] = columnSum[row - 1][col] + matrix[row][col];
            }
        }

        // Calculate matrixSum
        // First populate the first row
        for(int col = 0; col < cols; ++col){
            matrixSum[0][col] = rowSum[0][col];
        }
        // Then the first column
        for(int row = 0; row < rows; ++row){
            matrixSum[row][0] = columnSum[row][0];
        }
        // Then the rest
        for(int row = 1; row < rows; ++row){
            for(int col = 1; col < cols; ++col){
                matrixSum[row][col] = matrixSum[row-1][col - 1] + rowSum[row][col] + columnSum[row][col] - matrix[row][col];
            }
        }

        // for(int row = 0; row < rows; ++row){
        //     for(int col = 0; col < cols; ++col){
        //         cout << matrixSum[row][col] << " ";
        //     }
        //     cout << endl;
        // }


    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        // cout << matrixSum[row2][col2] << endl << matrixSum[row1][col2] << endl <<  matrixSum[row2][col1] << endl <<  matrixSum[row1][col1] << endl << endl << endl;
        int fullRectangle = matrixSum[row2][col2];
        if(row1 == 0 && col1 == 0){
            return fullRectangle;
        }
        if(row1 == 0 && col1 != 0){
            return fullRectangle - matrixSum[row2][col1 - 1];
        }
        if(row1 != 0 && col1 == 0){
            return fullRectangle - matrixSum[row1 - 1][col2];
        }
        return fullRectangle - matrixSum[row1 - 1][col2] - matrixSum[row2][col1 - 1] +  matrixSum[row1 - 1][col1 - 1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */