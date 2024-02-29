# Instructions:
# When you finish:
# 1. In the same terminal, type '../../scripts/saveTerminal.sh'
# 2. Open the command palette (Ctrl+shift+P on Windows, Command+Shift+P on Mac) 
#    and search for: Disable Saving Files
# 3. Press Ctrl+alt+R on Windows(Ctrl+Option+R on Mac) to stop recording your keystrokes 

class Solution(object):
    """
    Given an m x n matrix `board` where each cell is a battleship 'X' or empty '.', 
    return the number of the battleships on `board`.
    Battleships can only be placed horizontally or vertically on `board`. 
    In other words, they can only be made of the shape 1 x k (1 row, k columns) 
    or k x 1 (k rows, 1 column), where k can be of any size. 
    We ensure that at least one horizontal or vertical cell separates between two battleships 
    (i.e., there are no adjacent battleships).
    """
    # Example 1:
    """
    -------------------------
    |     |     |     |     |
    |  X  |     |     |  X  |
    -------------------------
    |     |     |     |     |
    |     |     |     |  X  |
    -------------------------
    |     |     |     |     |
    |     |     |     |  X  |
    -------------------------

    Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    Output: 2
    """
    # Example 2:
    """
    Input: board = [["."]]
    Output: 0
    """

    # Constraints:
    """
    - m == board.length
    - n == board[i].length
    - 1 <= m, n <= 200
    - board[i][j] is either '.' or 'X'
    """

    def countBattleships(self, board):
        count=0
        n=len(board[0])
        m=len(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='X':
                    count+=1
                    board[i][j]='.'
                    for t in range(j+1,n):
                        if board[i][t]=='.':
                            break
                        board[i][t]='.'
                    for t in range(i+1,m):
                        if board[t][j]=='.':
                            break
                        board[t][j]='.'
        return count
