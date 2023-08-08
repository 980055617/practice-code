import random
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.list_map = {}

    def insert(self, val: int) -> bool:
        # if in dict
        if (val in self.list_map):
            return False

        # maintaing dict and list
        self.list_map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # if not in dict
        if (val not in self.list_map):
            return False

        #swich last element and the element we want to remove
        val_pos = self.list_map[val]
        self.list_map[self.list[-1]] = val_pos
        self.list[val_pos], self.list[-1] =  self.list[-1], self.list[val_pos]

        # pop last element(the element we want to remove)
        self.list.pop()
        self.list_map.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    solution = RandomizedSet()
    print(solution.insert(1))
    print(solution.remove(2))
    print(solution.insert(2))
    print(solution.getRandom())
    print(solution.remove(1))
    print(solution.insert(2))
    print(solution.getRandom())
