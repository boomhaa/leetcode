# link to the problem - https://leetcode.com/problems/design-hashmap/

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

# link to submission - https://leetcode.com/submissions/detail/705429407/

class MyHashMap:

    def __init__(self):
        self.hash_map={}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key]=value

    def get(self, key: int) -> int:
        return self.hash_map.get(key,-1)

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]