class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        ret = self.cache.pop(key)
        self.cache[key] = ret

        return ret
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            for ret in self.cache:
                break
            self.cache.pop(ret)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)