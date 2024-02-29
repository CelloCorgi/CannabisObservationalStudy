#leetcode test size:27
# size: 2 checkrun + 2 example + 8 edge + 12 simple + 12 large = 36
from medium3 import Solution
import random
import string
import unittest
import time
import timeout_decorator
import collections
import copy

def genBoard( m, n, k=0):
        '''
        Generates a board of size m x n, with k battleships, with the restraint that
        battleships can only be placed horizontally or vertically on board. In other
        words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 
        (k rows, 1 column), where k can be of any size. At least one horizontal or 
        vertical cell separates between two battleships (i.e., there are no adjacent
        battleships).

        Returns a tuple (board, time_reference_solution)
        '''
        assert m >= 1 and n >= 1 and m <= 200 and n <= 200
        assert k >= 0 and k <= m * (n // 2 + n % 2)

        board = [['.' for _ in range(n)] for _ in range(m)]

        odd = [j for j in range(0, n, 2)]
        even = [j for j in range(1, n, 2)]
        starting_pos = random.sample(
            [[i, j] for i in range(m) for j in (odd, even)[i%2]], k=k)
        for i, j in starting_pos:
            board[i][j] = 'X'

        def valid(i, j, allow):
            nonlocal m, n, board
            if board[i][j] == 'X':
                return False
            for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii, jj = ii + i, jj + j
                if ii >= m or jj >= n or ii < 0 or jj < 0 or (ii, jj) == allow:
                    continue
                if board[ii][jj] == 'X':
                    return False
            return True
        
        for cur in starting_pos:
            d = 0 if random.random() < 0.5 else 1
            start = tuple(cur)
            while cur[d] + 1 < (m, n)[d]:
                allow = tuple(cur)
                cur[d] += 1
                if random.random() > 0.8 or not valid(cur[0], cur[1], allow):
                    break
                board[cur[0]][cur[1]] = 'X'
                if random.random() > 0.9:
                    board[start[0]][start[1]] = '.'

        return board

def correct_solution(board):
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


random.seed(10)

class SomeTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    
    @timeout_decorator.timeout(0.1)
    def test_checkrun1(self):
        solution=Solution()
        board=[['.']]
        solution.countBattleships(board)

    @timeout_decorator.timeout(0.1)
    def test_checkrun2(self):
        solution=Solution()
        board=[['.','.']]
        solution.countBattleships(board)

    @timeout_decorator.timeout(0.1)
    def test_example1(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
        assert(solution.countBattleships(board)==2)

    @timeout_decorator.timeout(0.1)
    def test_example2(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["."]]
        assert(solution.countBattleships(board)==0)

    @timeout_decorator.timeout(0.1)
    def test_edge1(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X"]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_edge2(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X",".","."]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_edge3(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X","X","X"]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_edge4(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".",".","."]]
        assert(solution.countBattleships(board)==0)

    @timeout_decorator.timeout(0.1)
    def test_edge5(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["."],
               ["X"],
               ["."]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_edge6(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X"],
               ["X"],
               ["X"]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_edge7(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["."],
               ["."],
               ["."]]
        assert(solution.countBattleships(board)==0)

    @timeout_decorator.timeout(0.1)
    def test_edge8(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".",".",".","."],
               [".",".",".","."],
               [".",".",".","."]]
        assert(solution.countBattleships(board)==0)

    @timeout_decorator.timeout(0.1)
    def test_simple1(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".","X","."],
               [".","X","."],
               [".",".","."]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_simple2(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".","X","."],
               [".",".","."],
               ["X","X","X"]]
        assert(solution.countBattleships(board)==2)

    @timeout_decorator.timeout(0.1)
    def test_simple3(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X","X","."],
               [".",".","X"]]
        assert(solution.countBattleships(board)==2)

    @timeout_decorator.timeout(0.1)
    def test_simple4(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X","X","X","X"],
               [".",".",".","."],
               ["X",".","X","X"],
               ["X",".",".","."]]
        assert(solution.countBattleships(board)==3)

    @timeout_decorator.timeout(0.1)
    def test_simple5(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".","X",".","X"],
                [".","X",".","X"],
                [".","X",".","X"],
                ["X",".",".","X"]]
        assert(solution.countBattleships(board)==3)

    @timeout_decorator.timeout(0.1)
    def test_simple6(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".",".",".",".","."],
                [".","X","X","X","."],
                [".",".",".",".","."],
                [".","X",".","X","."],
                [".","X",".","X","."]]
        assert(solution.countBattleships(board)==3)

    @timeout_decorator.timeout(0.1)
    def test_simple7(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X","X","X","X","X"],
                [".",".",".",".","."],
                ["X","X","X","X","X"],
                [".",".",".",".","."],
                [".",".",".",".","."]]
        assert(solution.countBattleships(board)==2)

    @timeout_decorator.timeout(0.1)
    def test_simple8(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".","X","X","X",".","."],
                [".",".",".",".","X","."],
                [".",".","X",".","X","."],
                [".","X",".",".","X","."],
                [".","X",".",".","X","."],
                [".",".",".","X",".","."]]
        assert(solution.countBattleships(board)==5)

    @timeout_decorator.timeout(0.1)
    def test_simple9(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".",".","X",".",".","."],
                [".",".","X",".",".","."],
                [".",".",".",".",".","."],
                [".",".",".",".",".","."],
                [".",".",".",".",".","."],
                [".",".",".",".",".","."]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_simple10(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[[".","."],
                ["X","."],
                ["X","."],
                ["X","."],
                ["X","."]]
        assert(solution.countBattleships(board)==1)

    @timeout_decorator.timeout(0.1)
    def test_simple11(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X","X",".","X",".",".","."]]
        assert(solution.countBattleships(board)==2)
    
    @timeout_decorator.timeout(0.1)
    def test_simple12(self):
        time.sleep(0.0001)
        solution=Solution()
        board=[["X"],
               ["X"],
               ["X"],
               ["."],
               ["."],
               ["X"],
               ["X"],
               ["."]]
        assert(solution.countBattleships(board)==2)

    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)