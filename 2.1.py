"""
1. Задача на циклический итератор.
Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту
(list, tuple, set, range, Range2, и т. д.), и когда достигнет последнего
элемента, начинать сначала.
"""


class CyclicIterator:
    def __init__(self, b):
        self.b = list(b)
        self.i = 0

    def __iter__(self):
        self.a = self.b[self.i]
        return self

    def __next__(self):
        x = self.a
        if self.i < len(self.b) - 1:
            self.i += 1
            self.a = self.b[self.i]
        elif self.i == len(self.b) - 1:
            self.i = 0
            self.a = self.b[self.i]
        return x


if __name__ == "__main__":
    check_list = [1, 2, 15, 0]
    check_tuple = (3, 4, 5, 6)
    check_set = {7, 8, 9, 10}
    check_range = range(1, 15)
    check_frozenset = frozenset(check_set)
    check_time = CyclicIterator([check_list, check_tuple, check_range, check_frozenset])
    for cyclic_iterator in check_time:
        for _ in cyclic_iterator:
            print(_)
