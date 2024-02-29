# leetcode test size:208
# size: 3 checkrun + 2 example + 6 edge + 23 simple + 20 large = 54
from easy2 import Solution
import random
import unittest
import time
import timeout_decorator
import collections
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BT:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        q = []
        q.append(self.root)
        while len(q):
            temp = q[0]
            q.pop(0)

            if not temp.left:
                temp.left = TreeNode(val)
                break
            q.append(temp.left)
            
            if not temp.right:
                temp.right = TreeNode(val)
                break
            q.append(temp.right)
def random_balanced_binary_tree(start:int, end:int, count:int = 1):
    bt = BT()
    for _ in range(count):
        rval = random.randint(start,end)
        bt.insert(rval)
    return bt.root

def random_binary_tree(size):
    root=TreeNode(size)
    left=[root]
    right=[root]
    size-=1
    while size>0:
        choice1=random.randint(1,10)
        if choice1<=5: # choose from left
            choice2=random.randint(0,len(left)-1)
            newNode=TreeNode(size)
            left[choice2].left=newNode
            left.pop(choice2)
            left.append(newNode)
            right.append(newNode)
        else:
            choice2=random.randint(0,len(right)-1)
            newNode=TreeNode(size)
            right[choice2].right=newNode
            right.pop(choice2)
            left.append(newNode)
            right.append(newNode)
        size-=1
    return root

def correct_solution(root):
    ans = []        
    def path(root, s):            
        if not root.left and not root.right:
            ans.append(s)            
        if root.left:
            path(root.left,s+"->"+str(root.left.val))
        if root.right:
            path(root.right,s+"->"+str(root.right.val))           
    path(root, str(root.val))
    return ans

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
        tree = TreeNode(1)
        solution.binaryTreePaths(tree)

    @timeout_decorator.timeout(0.1)
    def test_checkrun2(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3))
        solution.binaryTreePaths(tree)

    @timeout_decorator.timeout(0.1)
    def test_checkrun3(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2),None)
        solution.binaryTreePaths(tree)

    @timeout_decorator.timeout(0.1)
    def test_example1(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_example2(self):
        solution=Solution()
        tree = TreeNode(1)
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_edge1(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,None),None)
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_edge2(self):
        solution=Solution()
        tree = TreeNode(1,None,TreeNode(2,None,None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_edge3(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,None),TreeNode(3,None,None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_edge4(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3,None,None),None),None)
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_edge5(self):
        solution=Solution()
        tree = TreeNode(1,None,TreeNode(2,None,TreeNode(3,None,None)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_edge6(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3)),None)
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple1(self):
        solution=Solution()
        tree = TreeNode(1,None,TreeNode(2,TreeNode(3),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple2(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(4),TreeNode(2,TreeNode(3),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple3(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3),None),TreeNode(4))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple4(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple5(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(4),TreeNode(2,None,TreeNode(3)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple6(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),None)
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple7(self):
        solution=Solution()
        tree = TreeNode(1,None,TreeNode(2,TreeNode(3),TreeNode(4)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple8(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3),None),TreeNode(4,TreeNode(5),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple9(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4,TreeNode(5),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple10(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4,TreeNode(5),None),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple11(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4,None,TreeNode(5)),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple12(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple13(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4),None),None),TreeNode(5))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple14(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3,None,TreeNode(4)),None),TreeNode(5))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple15(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer
    
    @timeout_decorator.timeout(0.1)
    def test_simple16(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,TreeNode(3),None),TreeNode(4,None,TreeNode(5)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple17(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3,TreeNode(4),None)),TreeNode(5))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple18(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3,None,TreeNode(4))),TreeNode(5))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple19(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4,TreeNode(5),None))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple20(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4,None,TreeNode(5)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple21(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4,None,TreeNode(5)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple22(self):
        solution=Solution()
        tree = TreeNode(1,TreeNode(2),TreeNode(3,None,TreeNode(4,TreeNode(5),None)))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

    @timeout_decorator.timeout(0.1)
    def test_simple23(self):
        solution=Solution()
        tree = TreeNode(1,None,TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5)))))
        correct_answer=correct_solution(tree)
        correct_answer.sort()
        user_answer=solution.binaryTreePaths(tree)
        user_answer.sort()
        assert user_answer==correct_answer

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)