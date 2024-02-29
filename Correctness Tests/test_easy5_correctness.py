# leetcode test size:208
# size: 2 checkrun + 3 example + 4 edge + 15 simple + 15 large = 39
from easy5 import Solution
import random
import unittest
import time
import copy
import timeout_decorator
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def copy_list(list):
    root=ListNode(list.val)
    cur=list.next
    curr=root
    while cur:
        curr.next=ListNode(cur.val)
        curr=curr.next
        cur=cur.next
    return root

def correct_solution(list1, list2):
    current=ListNode(0)
    head=current
    while list1 and list2:
        if list1.val<=list2.val:
            current.next=list1
            list1=list1.next
        else:
            current.next=list2
            list2=list2.next
        current=current.next
    if list1:
        current.next=list1
    elif list2:
        current.next=list2
    return head.next

def print_list(head):
    plist=[]
    while head:
        plist.append(head.val)
        head=head.next
    return plist

random.seed(10)

def generate_list(start,end,size):
    randomlist = [random.randrange(start, end, 1) for i in range(size)]
    randomlist.sort()
    cur=1
    root=ListNode(randomlist[0])
    curNode=root
    while cur<size:
        curNode.next=ListNode(randomlist[cur])
        curNode=curNode.next
        cur+=1
    return root

class SomeTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    @timeout_decorator.timeout(0.1)
    def test_checkrun1(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(2,ListNode(4)))
        inputList2=ListNode(1,ListNode(3,ListNode(4)))
        Solution().mergeTwoLists(inputList1,inputList2)

    @timeout_decorator.timeout(0.1)
    def test_checkrun2(self):
        time.sleep(0.0001)
        inputList1=ListNode(2)
        inputList2=ListNode(1)
        Solution().mergeTwoLists(inputList1,inputList2)

    @timeout_decorator.timeout(0.1)
    def test_example1(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(2,ListNode(4)))
        inputList2=ListNode(1,ListNode(3,ListNode(4)))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,1,2,3,4,4])

    @timeout_decorator.timeout(0.1)
    def test_example2(self):
        time.sleep(0.0001)
        inputList1=None
        inputList2=None
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(not answer)

    @timeout_decorator.timeout(0.1)
    def test_example3(self):
        time.sleep(0.0001)
        inputList1=None
        inputList2=ListNode(0)
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[0])

    @timeout_decorator.timeout(0.1)    
    def test_edge1(self):
        time.sleep(0.0001)
        inputList1=None
        inputList2=ListNode(-1)
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-1])

    @timeout_decorator.timeout(0.1)
    def test_edge2(self):
        time.sleep(0.0001)
        inputList1=None
        inputList2=ListNode(1,ListNode(2))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,2])

    @timeout_decorator.timeout(0.1)    
    def test_edge3(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(2))
        inputList2=ListNode(1,ListNode(2))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,1,2,2])

    @timeout_decorator.timeout(0.1)    
    def test_edge4(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(1,ListNode(1,ListNode(1))))
        inputList2=ListNode(1,ListNode(1,ListNode(1,ListNode(1))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,1,1,1,1,1,1,1])

    @timeout_decorator.timeout(0.1)
    def test_simple1(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(2,ListNode(5,ListNode(8))))
        inputList2=None
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,2,5,8])

    @timeout_decorator.timeout(0.1)
    def test_simple2(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(2,ListNode(5,ListNode(8))))
        inputList2=ListNode(1,ListNode(2,ListNode(5,ListNode(8))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,1,2,2,5,5,8,8])

    @timeout_decorator.timeout(0.1)
    def test_simple3(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(1,ListNode(1,ListNode(1,ListNode(1,ListNode(1))))))
        inputList2=None
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,1,1,1,1,1])

    @timeout_decorator.timeout(0.1)
    def test_simple4(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(1,ListNode(1,ListNode(1,ListNode(1,ListNode(1))))))
        inputList2=ListNode(-1,ListNode(-1,ListNode(-1,ListNode(1,ListNode(1,ListNode(1))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-1,-1,-1,1,1,1,1,1,1,1,1,1])

    @timeout_decorator.timeout(0.1)
    def test_simple5(self):
        time.sleep(0.0001)
        inputList1=ListNode(3,ListNode(3,ListNode(6,ListNode(9,ListNode(10,ListNode(10))))))
        inputList2=ListNode(1,ListNode(4,ListNode(4,ListNode(5,ListNode(10,ListNode(11))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,3,3,4,4,5,6,9,10,10,10,11])

    @timeout_decorator.timeout(0.1)
    def test_simple6(self):
        time.sleep(0.0001)
        inputList1=ListNode(-11,ListNode(-4,ListNode(-1,ListNode(0,ListNode(0,ListNode(0))))))
        inputList2=ListNode(-5,ListNode(-5,ListNode(-2,ListNode(-1,ListNode(1,ListNode(1,ListNode(3,ListNode(3))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-11,-5,-5,-4,-2,-1,-1,0,0,0,1,1,3,3])

    @timeout_decorator.timeout(0.1)
    def test_simple7(self):
        time.sleep(0.0001)
        inputList1=ListNode(-5,ListNode(-5,ListNode(-2,ListNode(-1,ListNode(1,ListNode(1,ListNode(3,ListNode(3))))))))
        inputList2=ListNode(-23,ListNode(2,ListNode(2,ListNode(5,ListNode(5,ListNode(11,ListNode(13,ListNode(13))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-23,-5,-5,-2,-1,1,1,2,2,3,3,5,5,11,13,13])

    @timeout_decorator.timeout(0.1)
    def test_simple8(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(3,ListNode(5,ListNode(7,ListNode(9,ListNode(11,ListNode(13,ListNode(15))))))))
        inputList2=ListNode(2,ListNode(4,ListNode(6,ListNode(8,ListNode(10,ListNode(12,ListNode(14,ListNode(16))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

    @timeout_decorator.timeout(0.1)
    def test_simple9(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(3,ListNode(5,ListNode(7,ListNode(9,ListNode(11,ListNode(13,ListNode(15))))))))
        inputList2=ListNode(2,ListNode(4,ListNode(6,ListNode(8,ListNode(10,ListNode(12,ListNode(14,ListNode(15,ListNode(16)))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16])

    @timeout_decorator.timeout(0.1)
    def test_simple10(self):
        time.sleep(0.0001)
        inputList1=ListNode(-1,ListNode(3,ListNode(5,ListNode(7,ListNode(9,ListNode(13,ListNode(13,ListNode(15,ListNode(15,ListNode(17))))))))))
        inputList2=ListNode(-2,ListNode(4,ListNode(6,ListNode(8,ListNode(10,ListNode(13,ListNode(14,ListNode(15,ListNode(16,ListNode(20))))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-2,-1,3,4,5,6,7,8,9,10,13,13,13,14,15,15,15,16,17,20])

    @timeout_decorator.timeout(0.1)
    def test_simple11(self):
        time.sleep(0.0001)
        inputList1=ListNode(1,ListNode(3,ListNode(5,ListNode(7,ListNode(9,ListNode(11,ListNode(13,ListNode(15))))))))
        inputList2=ListNode(-22,ListNode(-14,ListNode(-6,ListNode(-2,ListNode(-1,ListNode(0,ListNode(0)))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-22,-14,-6,-2,-1,0,0,1,3,5,7,9,11,13,15])

    @timeout_decorator.timeout(0.1)
    def test_simple12(self):
        time.sleep(0.0001)
        inputList1=ListNode(-22,ListNode(-14,ListNode(-6,ListNode(-2,ListNode(-1,ListNode(0,ListNode(0)))))))
        inputList2=ListNode(1,ListNode(3,ListNode(5,ListNode(7,ListNode(9,ListNode(11,ListNode(13,ListNode(15))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-22,-14,-6,-2,-1,0,0,1,3,5,7,9,11,13,15])

    @timeout_decorator.timeout(0.1)
    def test_simple13(self):
        time.sleep(0.0001)
        inputList1=ListNode(-11,ListNode(3,ListNode(5,ListNode(7,ListNode(7,ListNode(8,ListNode(8)))))))
        inputList2=ListNode(-5,ListNode(-4,ListNode(3,ListNode(3,ListNode(5,ListNode(6,ListNode(7,ListNode(11,ListNode(16)))))))))
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==[-11,-5,-4,3,3,3,5,5,6,7,7,7,8,8,11,16])

    @timeout_decorator.timeout(0.1)
    def test_simple14(self):
        time.sleep(0.0001)
        inputList1=generate_list(-10,10,5)
        inputList2=generate_list(-10,10,5)
        inputList11=copy.deepcopy(inputList1)
        inputList12=copy.deepcopy(inputList2)
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==print_list(correct_solution(inputList11,inputList12)))

    @timeout_decorator.timeout(0.1)
    def test_simple15(self):
        time.sleep(0.0001)
        inputList1=generate_list(-10,10,20)
        inputList2=generate_list(-10,10,20)
        inputList11=copy.deepcopy(inputList1)
        inputList12=copy.deepcopy(inputList2)
        answer=print_list(Solution().mergeTwoLists(inputList1,inputList2))
        assert(answer==print_list(correct_solution(inputList11,inputList12)))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)