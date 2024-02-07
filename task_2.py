class Immutable:
    def __new__(cls, value):
        instance = super().__new__(cls)
        instance._value = value
        return instance

    def get_value(self):
        return self._value

    def __setattr__(self, name, value):
        if name != "_value":
            raise AttributeError("Immutable object does not support attribute assignment")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        raise AttributeError("Immutable object does not support attribute deletion")


immutable_str = Immutable("Hello, World!")
print(immutable_str.get_value())
# immutable_str.value = "New Value"


immutable_int = Immutable(42)
print(immutable_int.get_value())
# immutable_int.value = 100


immutable_list = Immutable([1, 2, 3])
print(immutable_list.get_value())
# immutable_list.value.append(4)


immutable_dict = Immutable({"key": "value"})
print(immutable_dict.get_value())
# immutable_dict.value["new_key"] = "new_value"
