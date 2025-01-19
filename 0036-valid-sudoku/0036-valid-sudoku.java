class Solution {

    public boolean isValidSudoku(char[][] board) {
        /*
        # Take each value
        # Validate in row for count 1
        # Validate in column for count 1
        # Validate 3x3 box for count 1
        # If any of the is invalid return False
        # Move to next element
        # Return True at end if no False found
        */
        for(int i = 0; i < 9; i ++) {
            for(int j = 0; j < 9; j++) {
                char value = board[i][j];
                if(value != '.') {
                    if (!validate(i, j, board)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public boolean validate(int r, int c, char[][] board) {
        int count = 0;
        for(int i = 0; i < 9; i++) {
            if (board[i][c] == board[r][c]) {
                count += 1;
            }
        }
        if (count >= 2) {
            return false;
        } else {
            count = 0;
        }
        for(int j = 0; j < 9; j++) {
            if (board[r][j] == board[r][c]) {
                count += 1;
            }
        }
        if (count >= 2) {
            return false;
        } else {
            count = 0;
        }
        int nr = r;
        int nc = c;
        nr -= r % 3;
        nc -= c % 3;
        for(int i = nr; i < nr + 3; i++) {
            for(int j = nc; j < nc + 3; j++) {
                if (board[i][j] == board[r][c]) {
                    count += 1;
                }
            }
        }
        if (count >= 2) {
            return false;
        } 
        return true;
    }
}