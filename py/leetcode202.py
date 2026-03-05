class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        slow = n
        fast = next(n)
        while fast != 1 and slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return fast == 1