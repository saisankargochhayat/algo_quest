# class LRUCache:

#     def __init__(self, capacity: int):
#         self.lru_dict = {}
#         self.maxcap = capacity
#         self.curr_vol = 0
#         self.count = 0

#     def get(self, key: int) -> int:
#         # This is O(1)
#         if key in self.lru_dict:
#             self.lru_dict[key][1] = self.count
#             self.count += 1
#             return self.lru_dict[key][0]
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.lru_dict:
#             self.lru_dict[key] = [value, self.count]
#             self.count += 1
#         elif self.curr_vol < self.maxcap:
#             self.lru_dict[key] = [value, self.count]
#             self.count += 1
#             self.curr_vol += 1
#         else:
#             minKey, minVal = None, float('inf')
#             for k in self.lru_dict.keys():
#                 if self.lru_dict[k][1] < minVal:
#                     minKey, minVal = k, self.lru_dict[k][1]
#             del self.lru_dict[minKey]
#             self.lru_dict[key] = [value, self.count]
#             self.count += 1

            
from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
