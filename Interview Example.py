#Problem: Add Two Numbers

def solution(num1, num2):
    return num1+num2

from nose.tools import assert_equal
# you may have to download nose, nose is basically a testing library

class SolutionTest(object):
    def test(self, sol):
        assert_equal(solution(2,2), 4)
        assert_equal(solution(4,4), 8)

        print("ALL TEST CASES PASSED")

t = SolutionTest()
t.test(solution())
# both should result true and print out the print statement
# if not true will get an AssertionError and tells you which is not equal