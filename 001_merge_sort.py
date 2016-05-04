"""
Merge Sort
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual([1, 2, 3, 4, 5], solution.mergeSort([4, 5, 3, 2, 1]))


class Solution(object):

    def mergeSort(self, nums):
        N = len(nums)
        if N == 0 or N == 1:
            return nums[:]

        return self.partition(self.mergeSort(nums[:N/2]),
                              self.mergeSort(nums[N/2:]))

    def partition(self, n1, n2):
        if n1 is None:
            return n2[:]
        if n2 is None:
            return n1[:]
        tmp = []
        i, j = 0, 0
        while i < len(n1) and j < len(n2):
            if n1[i] < n2[j]:
                tmp.append(n1[i])
                i += 1
            else:
                tmp.append(n2[j])
                j += 1

        tmp.extend(n1[i:])
        tmp.extend(n2[j:])
        return tmp
