# https://leetcode.com/problems/design-hashmap/description/

class MyHashMap:

    def __init__(self):
        self.theMap = {}

    def put(self, key: int, value: int) -> None:
        self.theMap[key]=value

    def get(self, key: int) -> int:
        try:
            return self.theMap[key]
        except:
            return -1


    def remove(self, key: int) -> None:
        try:
            del self.theMap[key]
        except:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)