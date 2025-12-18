"""
Searching Algorithms Implementation
Author: Abdul Malik Sk
"""

def linear_search(arr, target):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Binary Search Algorithm (requires sorted array)
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Binary Search - Recursive Implementation
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    """
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the algorithms
if __name__ == "__main__":
    test_arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    target = 23
    
    print("Array:", test_arr)
    print(f"Linear Search for {target}:", linear_search(test_arr, target))
    print(f"Binary Search for {target}:", binary_search(test_arr, target))
    print(f"Binary Search Recursive for {target}:", 
          binary_search_recursive(test_arr, target, 0, len(test_arr) - 1))