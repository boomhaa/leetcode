# link to the problem - https://leetcode.com/problems/map-sum-pairs/

# Design a map that allows you to do the following:
# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Implement the MapSum class:
# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

# link to submission - https://leetcode.com/submissions/detail/764793767/

class MapSum:

	def __init__(self):
		self.cache = {}

	def insert(self, key: str, val: int) -> None:
		self.cache[key] = val

	def sum(self, prefix: str) -> int:
		len_prefix = len(prefix)
		total = 0
		for word, value in self.cache.items():
			if word[: len_prefix] == prefix:
				total += value

		return total