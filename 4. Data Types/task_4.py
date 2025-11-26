from operator import index

from fontTools.mtiLib import bucketizeRules


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # A simple hash function using the length of the key
        return len(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i in bucket:
            if i.key == key:
                i.value = value
        bucket.append(KeyValuePair(key, value))

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i in bucket:
            if i.key == key:
                return i.value
        return default

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for j,i in enumerate(bucket):
            if i.key == key:
                del bucket[j]
                return True
        return False

    def keys(self):
        all_keys = []
        for i in self.buckets:
            for j in i:
                all_keys.append(j.key)
        return all_keys

    def values(self):
        all_values = []
        for i in self.buckets:
            for j in i:
                all_values.append(j.value)
        return all_values

    def items(self):
        all_items = []
        for i in self.buckets:
            for j in i:
                all_items.append((j.key, j.value))
        return all_items


my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())