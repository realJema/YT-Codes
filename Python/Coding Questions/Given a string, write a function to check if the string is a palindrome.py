'''
Name: Given a binary tree, write a function to find the maximum depth of the tree.
Author: @realJema 
Date: 08/2023
'''

import random
import unittest


def find_kth_smallest(numbers, k):
  """
  Finds the kth smallest number in a list of numbers.

  Args:
    numbers: The list of numbers.
    k: The index of the smallest number to find.

  Returns:
    The kth smallest number in the list.
  """

  if len(numbers) <= k:
    raise ValueError("k is larger than the length of the list")

  # Sort the list.
  numbers.sort()

  # Return the kth smallest number.
  return numbers[k - 1]


class TestFindKthSmallest(unittest.TestCase):

  def test_find_kth_smallest_1(self):
    """Tests whether the find_kth_smallest function correctly finds the kth smallest number in a list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    k = 2
    self.assertEqual(find_kth_smallest(numbers, k), 3)

  def test_find_kth_smallest_2(self):
    """Tests whether the find_kth_smallest function correctly finds the kth smallest number in a list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    k = 5
    self.assertEqual(find_kth_smallest(numbers, k), 5)

  def test_find_kth_smallest_3(self):
    """Tests whether the find_kth_smallest function correctly raises an error if k is larger than the length of the list."""
    numbers = [1, 2, 3, 4, 5]
    k = 6
    with self.assertRaises(ValueError):
      find_kth_smallest(numbers, k)


if __name__ == "__main__":
  unittest.main()