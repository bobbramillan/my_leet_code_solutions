

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:28:41 2023

@author: Bob Bramillan

Problem Statement (Two Sum):
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""

def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    index_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in index_dict:
            # Return the indices of the two numbers
            return [index_dict[complement], i]

        # Add the current number and its index to the dictionary
        index_dict[num] = i

    # If no solution is found, return an empty list
    return []
import pytest

def test_two_sum():
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

    # Test case 3
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]

    # Add more test cases as needed

# Run the tests if this script is executed
if __name__ == "__main__":
    pytest.main([__file__])