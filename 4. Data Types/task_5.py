class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        if not self.contains(value):
            index = self._hash(value)
            self.buckets[index].append(value)

    def remove(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]

        for i, item in enumerate(bucket):
            if item == value:
                del bucket[i]
                return True
        return False

    def contains(self, value):
        index = self._hash(value)
        return value in self.buckets[index]

    def elements(self):
        elements_list = []
        for bucket in self.buckets:
            elements_list.extend(bucket)
        return elements_list



my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())