# leetcode test size:106
# size: 3 checkrun + 2 example + 4 edge + 18 simple + 17 large = 44
from easy1 import Solution
import random
import string
import time
import unittest
import timeout_decorator

def correct_solution(s):
    stack = []
    answer = ''
    for letter in s:
        if len(stack):
            if stack[-1] == letter:
                stack.pop()
                continue
        stack.append(letter)
    for i in stack:
        answer+=i
    return answer

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
        solution.removeDuplicates("a")

    @timeout_decorator.timeout(0.1)
    def test_checkrun2(self):
        solution=Solution()
        solution.removeDuplicates("abc")

    @timeout_decorator.timeout(0.1)
    def test_checkrun3(self):
        solution=Solution()
        solution.removeDuplicates("aaa")

    @timeout_decorator.timeout(0.1)
    def test_example1(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("abbaca")==solution.removeDuplicates("abbaca")

    @timeout_decorator.timeout(0.1)
    def test_example2(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("azxxzy")==solution.removeDuplicates("azxxzy")

    @timeout_decorator.timeout(0.1)
    def test_edge1(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("a")==solution.removeDuplicates("a")

    @timeout_decorator.timeout(0.1)
    def test_edge2(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("aa")==solution.removeDuplicates("aa")

    @timeout_decorator.timeout(0.1)
    def test_edge3(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("aaa")==solution.removeDuplicates("aaa")

    @timeout_decorator.timeout(0.1)
    def test_edge4(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("aaaa")==solution.removeDuplicates("aaaa")

    @timeout_decorator.timeout(0.1)
    def test_simple1(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("ab")==solution.removeDuplicates("ab")

    @timeout_decorator.timeout(0.1)
    def test_simple2(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("aab")==solution.removeDuplicates("aab")
    
    @timeout_decorator.timeout(0.1)
    def test_simple3(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("ssddff")==solution.removeDuplicates("ssddff")

    @timeout_decorator.timeout(0.1)
    def test_simple4(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("aabbbccdddcbbdp")==solution.removeDuplicates("aabbbccdddcbbdp")

    @timeout_decorator.timeout(0.1)
    def test_simple5(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("abdueifiisofhfjsff")==solution.removeDuplicates("abdueifiisofhfjsff")

    @timeout_decorator.timeout(0.1)
    def test_simple6(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("soppofafhircpddsjioaaaf")==solution.removeDuplicates("soppofafhircpddsjioaaaf")

    @timeout_decorator.timeout(0.1)
    def test_simple7(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("fhuuushakfjjffffkkalsmfns")==solution.removeDuplicates("fhuuushakfjjffffkkalsmfns")

    @timeout_decorator.timeout(0.1)
    def test_simple8(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("eeuahfjsk")==solution.removeDuplicates("eeuahfjsk")

    @timeout_decorator.timeout(0.1)
    def test_simple9(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("abchdusiglw")==solution.removeDuplicates("abchdusiglw")

    @timeout_decorator.timeout(0.1)
    def test_simple10(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("fffiiiifsssssssssllllllffffffiiif")==solution.removeDuplicates("fffiiiifsssssssssllllllffffffiiif")

    @timeout_decorator.timeout(0.1)
    def test_simple11(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("pppwwooorhhhhfuaiiiigeah")==solution.removeDuplicates("pppwwooorhhhhfuaiiiigeah")

    @timeout_decorator.timeout(0.1)
    def test_simple12(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("chsuuufiqfllafksuifouqwirehjkahjsd")==solution.removeDuplicates("chsuuufiqfllafksuifouqwirehjkahjsd")

    @timeout_decorator.timeout(0.1)
    def test_simple13(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("aabccb")==solution.removeDuplicates("aabccb")

    @timeout_decorator.timeout(0.1)
    def test_simple14(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("abccba")==solution.removeDuplicates("abccba")

    @timeout_decorator.timeout(0.1)
    def test_simple15(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("thjkkkjjk")==solution.removeDuplicates("thjkkkjjk")

    @timeout_decorator.timeout(0.1)
    def test_simple16(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("ertyyyyyttytr")==solution.removeDuplicates("ertyyyyyttytr")

    @timeout_decorator.timeout(0.1)
    def test_simple17(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("abccbaxyz")==solution.removeDuplicates("abccbaxyz")
    
    @timeout_decorator.timeout(0.1)
    def test_simple18(self):
        time.sleep(0.0001)
        solution=Solution()
        assert correct_solution("ijtbttbbt")==solution.removeDuplicates("ijtbttbbt")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner(verbosity=0).run(suite)