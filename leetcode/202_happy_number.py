class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(n: int) -> int:
            return sum(int(num)**2 for num in str(n))

        slow = n
        fast = n

        while slow != fast and fast != 1:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

        return fast == 1
