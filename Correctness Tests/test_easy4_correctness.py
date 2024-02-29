#leetcode testsize：37
# size: 2 checkrun + 3 example + 3 edge + 16 simple + 12 large = 36
from easy4 import Solution
import random
import string
import unittest
import timeout_decorator
import time
def correct_solution(arr):
    arr.sort()
    min_dif=arr[1]-arr[0]
    res=[[arr[0],arr[1]]]
    
    for i in range(1,len(arr)-1):
        q=[]
        if((arr[i+1]-arr[i])<min_dif):
            min_dif=arr[i+1]-arr[i]
            res=[]
        if(arr[i+1]-arr[i]==min_dif):
            q=[arr[i],arr[i+1]]
            res.append(q)
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
        arr=[1,1]
        Solution().minimumAbsDifference(arr)

    @timeout_decorator.timeout(0.1)
    def test_checkrun2(self):
        arr=[1,2,3,4]
        Solution().minimumAbsDifference(arr)

    @timeout_decorator.timeout(0.1)
    def test_example1(self):
        time.sleep(0.0001)
        arr=[4,2,1,3]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_example2(self):
        time.sleep(0.0001)
        arr=[1,3]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_example3(self):
        time.sleep(0.0001)
        arr=[3,8,-10,23,19,-4,-14,27]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_edge1(self):
        time.sleep(0.0001)
        arr=[-2,-1,1,2]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_edge2(self):
        time.sleep(0.0001)
        arr=[0,1]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_edge3(self):
        time.sleep(0.0001)
        arr=[-1000000,1000000,-999999,999999]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple1(self):
        time.sleep(0.0001)
        arr=[3,2]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple2(self):
        time.sleep(0.0001)
        arr=[-1,-2]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)
    
    @timeout_decorator.timeout(0.1)
    def test_simple3(self):
        time.sleep(0.0001)
        arr=[0,1,2]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple4(self):
        time.sleep(0.0001)
        arr=[12,10,11]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple5(self):
        time.sleep(0.0001)
        arr=[0,-1,-2]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple6(self):
        time.sleep(0.0001)
        arr=[0,-10,10]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple7(self):
        time.sleep(0.0001)
        arr=[-3,1,0,3]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)
    
    @timeout_decorator.timeout(0.1)
    def test_simple8(self):
        time.sleep(0.0001)
        arr=[1,-1,0,2,-2]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple9(self):
        time.sleep(0.0001)
        arr=[11,-1,0,1,-5,2,-4,3,4,-2,-9]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple10(self):
        time.sleep(0.0001)
        arr=[0,4,-2,1,2,3,9,-4,5,8,6,-5]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple11(self):
        time.sleep(0.0001)
        arr=[130,-78,-161,190,-83,179,257,-233,203,233,-273,36,43,93,169,-260,-7,168,117,50,-74,-54,137,-250,151,-85,21,35,-28]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple12(self):
        time.sleep(0.0001)
        arr=[0,10,20,22,29,24,16,19,11,42,40,34,37,30,39]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple13(self):
        time.sleep(0.0001)
        arr=[0,5,2,8,3,-2,-7,-6,-9,-30,-17,13,16,12,23,26,44,78]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple14(self):
        time.sleep(0.0001)
        arr=[188,9,-189,-112,165,4,-141,179,-154,258,53,71,201,204,121,215,259,-22,34,-213,-88,-192,118,-221,130,-86,209]
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple15(self):
        time.sleep(0.0001)
        arr=random.sample(range(-10000,10000),10)
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

    @timeout_decorator.timeout(0.1)
    def test_simple16(self):
        time.sleep(0.0001)
        arr=random.sample(range(-10000,10000), 20)
        answer=Solution().minimumAbsDifference(arr)
        #answer.sort()
        correct_answer=correct_solution(arr)
        correct_answer.sort()
        assert(correct_answer==answer)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)