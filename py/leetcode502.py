class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w > max(capital):
            return w + sum(nlargest(k, profits))

        n = len(profits)
        curr = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])

        qp = []
        for _ in range(k):
            while curr < n and arr[curr][0] <= w:
                heappush(qp, -arr[curr][1])
                curr += 1
            if qp:
                w -= heappop(qp)
            else:
                break

        return w