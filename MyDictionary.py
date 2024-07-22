class Dictionary:  # Linear probing

    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = self.has_function(key)

        if self.slot[hash_value] is None:
            self.slot[hash_value] = key
            self.data[hash_value] = value

        else:

            if self.slot[hash_value] == key:
                self.data[hash_value] = value

            else:

                while self.slot[hash_value] is not None and self.slot[hash_value] != key:
                    hash_value = self.rehash(hash_value)

                self.slot[hash_value] = key
                self.data[hash_value] = value

    def __setitem__(self, key, value):
        self.put(key, value)

    def has_function(self, key):
        return abs(hash(key)) % self.size

    def rehash(self, prev_hash):
        return (prev_hash + 1) % self.size

    def get(self, key):
        hash_value = self.has_function(key)
        current_hash = hash_value
        while self.slot[current_hash] is not None:
            if self.slot[current_hash] == key:
                return self.data[current_hash]

            current_hash = self.rehash(current_hash)

            if current_hash == hash_value:
                return "item not found"

        return "item not found"



d = Dictionary(3)

print(d.slot, "\n", d.data)
d["python"] = 34
d["java"] = 65
d["c++"] = 554
print("*" * 80)
print(d.slot, "\n", d.data)

python_value = d.get("java")

print(python_value)
