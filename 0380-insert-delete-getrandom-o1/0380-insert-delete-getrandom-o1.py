#Time Complexity : Average O(1)
#Space Compelxity : O(n)
import random
class RandomizedSet:

    def __init__(self):
        self.nums_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.nums_map:
            return False
        self.nums_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.nums_map:
            return False
        last_elem = self.nums[-1]
        index_to_remove_elements = self.nums_map[val]
        self.nums_map[last_elem] = index_to_remove_elements
        self.nums[index_to_remove_elements] = last_elem

        self.nums[-1] = val
        self.nums.pop()
        self.nums_map.pop(val)
        return True


    def getRandom(self) -> int:
        rand_num = random.choice(self.nums)
        return rand_num


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()