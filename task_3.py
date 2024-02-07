class CustomComparator:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __int__(self):
        if isinstance(self.value, str):
            return len(self.value)
        elif isinstance(self.value, int):
            return len(str(self.value))
        elif isinstance(self.value, list):
            return len(self.value)
        elif isinstance(self.value, dict):
            if any(isinstance(value, dict) for value in self.value.values()):
                raise TypeError("Unsupported type")
            else:
                return sum(len(str(k)) for k in self.value.keys()) + sum(len(str(v)) for v in self.value.values())
        else:
            raise TypeError("Unsupported type")


print(CustomComparator("hello") > CustomComparator({"a": 1, "b": 2}))
print(CustomComparator(123) <= CustomComparator([4, 5, 6]))
print(CustomComparator([1, 2, 3]) == CustomComparator(789))
print(CustomComparator({"a": 1, "b": 2}) > CustomComparator("1234"))
print(CustomComparator([1, 2, 3]) <= CustomComparator({"a": 1, "b": 2, 5: {1: 1}}))