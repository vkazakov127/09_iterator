# -*- coding: utf-8 -*-

class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start - 1  # Счётчик итератора
        return self

    def __next__(self):
        self.i += 1  # Инкремент счётчика итератора
        if self.i % 2: # Если нечётное число, то следующий элемент
            self.i += 1  # Ещё один инкремент счётчика итератора
        if self.i >= self.start:
            if self.i > self.end:
                raise StopIteration()
            return self.i


# Вызов итератора
en = EvenNumbers(10, 25)
print(f'Чётные числа от {en.start} до {en.end}:')
for i in en:
    print(i)

