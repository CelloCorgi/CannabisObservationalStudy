
#leetcode test size：23
# size: 3 checkrun + 3 example + 10 edge + 16 simple + 16 large = 48
from medium6 import Solution
import random
import string
import unittest
import time
import timeout_decorator

def generate_matrix(row,col):
    matrix=[]
    count=0
    for i in range(row):
        roww=[]
        for j in range(col):
            roww.append(count)
            count+=1
        matrix.append(roww)
    return matrix

def solution(matrix):
    res = []
    left, right = 0, len(matrix[0]) 
    top, bottom = 0, len(matrix)
    
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        if not (left < right and top < bottom):
            break
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res


random.seed(10)


class SomeTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    @timeout_decorator.timeout(0.1)
    def test_checkrun1(self):
        matrix=[[1]]
        Solution().spiralOrder(matrix)

    @timeout_decorator.timeout(0.1)
    def test_checkrun2(self):
        matrix=[[1,2]]
        Solution().spiralOrder(matrix)

    @timeout_decorator.timeout(0.1)
    def test_checkrun3(self):
        matrix=[[1],[2]]
        Solution().spiralOrder(matrix)

    @timeout_decorator.timeout(0.1)
    def test_example1(self):
        time.sleep(0.0001)
        matrix=[[1,2,3], [4,5,6],[7,8,9]]
        matrix1=[[1,2,3], [4,5,6],[7,8,9]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_example2(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        matrix1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_example3(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        matrix1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))
    
    @timeout_decorator.timeout(0.1)
    def test_edge1(self):
        time.sleep(0.0001)
        matrix=[[1]]
        matrix1=[[1]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge2(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4]]
        matrix1=[[1,2,3,4]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))
    
    @timeout_decorator.timeout(0.1)
    def test_edge3(self):
        time.sleep(0.0001)
        matrix=[[1],[2],[3],[4]]
        matrix1=[[1],[2],[3],[4]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge4(self):
        time.sleep(0.0001)
        matrix=[[1,2],[3,4],[5,6],[7,8]]
        matrix1=[[1,2],[3,4],[5,6],[7,8]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge5(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4],[5,6,7,8]]
        matrix1=[[1,2,3,4],[5,6,7,8]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge6(self):
        time.sleep(0.0001)
        matrix=[[1],[2]]
        matrix1=[[1],[2]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge7(self):
        time.sleep(0.0001)
        matrix=[[1,2]]
        matrix1=[[1,2]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge8(self):
        time.sleep(0.0001)
        matrix=[[1,2],[3,4]]
        matrix1=[[1,2],[3,4]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge9(self):
        time.sleep(0.0001)
        matrix=[[1,2],[3,4],[5,6]]
        matrix1=[[1,2],[3,4],[5,6]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_edge10(self):
        time.sleep(0.0001)
        matrix=[[1,2,3],[4,5,6]]
        matrix1=[[1,2,3],[4,5,6]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple1(self):
        time.sleep(0.0001)
        matrix=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
        matrix1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple2(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
        matrix1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple3(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
        matrix1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple4(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        matrix1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple5(self):
        time.sleep(0.0001)
        matrix=[[1],[2],[3],[4],[5]]
        matrix1=[[1],[2],[3],[4],[5]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple6(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4,5]]
        matrix1=[[1,2,3,4,5]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple7(self):
        time.sleep(0.0001)
        matrix=[[1,2],[3,4],[5,6],[7,8],[9,10]]
        matrix1=[[1,2],[3,4],[5,6],[7,8],[9,10]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple8(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4,5],[6,7,8,9,10]]
        matrix1=[[1,2,3,4,5],[6,7,8,9,10]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple9(self):
        time.sleep(0.0001)
        matrix=[[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12],
                [13,14,15]]
        matrix1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple10(self):
        time.sleep(0.0001)
        matrix=[[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]]
        matrix1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple11(self):
        time.sleep(0.0001)
        matrix=generate_matrix(2,10)
        matrix1=generate_matrix(2,10)
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple12(self):
        time.sleep(0.0001)
        matrix=generate_matrix(10,2)
        matrix1=generate_matrix(10,2)
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple13(self):
        time.sleep(0.0001)
        matrix=generate_matrix(5,10)
        matrix1=generate_matrix(5,10)
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple14(self):
        time.sleep(0.0001)
        matrix=generate_matrix(10,5)
        matrix1=generate_matrix(10,5)
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple15(self):
        time.sleep(0.0001)
        matrix=generate_matrix(4,5)
        matrix1=generate_matrix(4,5)
        assert(Solution().spiralOrder(matrix)==solution(matrix1))

    @timeout_decorator.timeout(0.1)
    def test_simple16(self):
        time.sleep(0.0001)
        matrix=generate_matrix(4,4)
        matrix1=generate_matrix(4,4)
        assert(Solution().spiralOrder(matrix)==solution(matrix1))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)
