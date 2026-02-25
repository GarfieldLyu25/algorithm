from random import choice

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.nums:
            idx = self.index[val]
            self.nums[idx] = self.nums[-1]
            self.index[self.nums[-1]] = idx
            del self.index[val]  #
            self.nums.pop()  #
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()