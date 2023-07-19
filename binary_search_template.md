# Binary search template

## generic template

```py
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) / 2
        if condition(mid):
            right = mid
        else:
            left = mid+1
    return left
```

## parts that need to be updated to fit a problem
- Correctly initialize the boundary variables `left` and `right`
- Decide the return value, is it `left`or `left-1`? **After exiting the while loop, left is the minimal k satisfying the `condition` function**
- Design the `condition` function.

## First bad version
```py
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
