class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = min_ans = s = 0
        for i,(g,c) in enumerate(zip(gas,cost)):
            s += g - c
            if s < min_ans:
                min_ans = s
                ans = i + 1
        if s < 0:
            return -1
        return ans