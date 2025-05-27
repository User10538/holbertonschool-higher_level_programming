#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.__iter__ = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def get_count(self):
        return self.count

    def __next__(self):
        item = next(self.__iter__)
        self.count = self.count + 1
        return item
