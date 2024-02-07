from typing import Union


class Kilogram:
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        if value >= 1000:
            raise ValueError("Значение килограммов не может быть больше или равно 1000")
        self.value = value

    def to_pounds(self) -> 'Pound':
        return Pound(self.value * 2.20462)

    def __add__(self, other: Union['Kilogram', 'Pound']) -> 'Kilogram':
        if isinstance(other, Kilogram):
            return Kilogram(self.value + other.value)
        elif isinstance(other, Pound):
            return Kilogram(self.value + other.to_kilograms().value)
        else:
            raise ValueError("Неподдерживаемый тип операции")

    def __sub__(self, other: Union['Kilogram', 'Pound']) -> 'Kilogram':
        if isinstance(other, Kilogram):
            return Kilogram(self.value - other.value)
        elif isinstance(other, Pound):
            return Kilogram(self.value - other.to_kilograms().value)
        else:
            raise ValueError("Неподдерживаемый тип операции")

    def increase(self, increment: float) -> None:
        if self.value + increment < 0:
            raise ValueError("Результат увеличения не может быть отрицательным")
        self.value += increment

    def __repr__(self) -> str:
        return f"{self.value} кг, {self.value * 1000} г "


class Pound:
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        if value >= 14:
            raise ValueError("Значение фунтов не может быть больше или равно 14")
        self.value = value

    def to_kilograms(self) -> 'Kilogram':
        return Kilogram(self.value / 2.20462)

    def __add__(self, other: Union) -> 'Pound':
        if isinstance(other, Pound):
            return Pound(self.value + other.value)
        elif isinstance(other, Kilogram):
            return Pound(self.value + other.to_pounds().value)
        else:
            raise ValueError("Неподдерживаемый тип операции")

    def __sub__(self, other) -> 'Pound':
        if isinstance(other, Pound):
            return Pound(self.value - other.value)
        elif isinstance(other, Kilogram):
            return Pound(self.value - other.to_pounds().value)
        else:
            raise ValueError("Неподдерживаемый тип операции")

    def increase(self, increment: float) -> None:
        if self.value + increment < 0:
            raise ValueError("Результат увеличения не может быть отрицательным")
        self.value += increment

    def __repr__(self) -> 'str':
        return f"{self.value} фунт, {self.value * 16} унций "


kg_obj1 = Kilogram(500)
kg_obj2 = Kilogram(1)
kg_obj2.increase(1)
print(kg_obj1 + kg_obj2)
print(kg_obj2.to_pounds())

print('=' * 40)

lb_obj1 = Pound(10)
lb_obj2 = Pound(3)
print(lb_obj1 + lb_obj2)
print(lb_obj1.to_kilograms())

print('=' * 40)

result = kg_obj1 + lb_obj1
print(result)
