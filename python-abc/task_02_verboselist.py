#!/usr/bin/env python3

class VerboseList(list):
    """
    Create a class named VerboseList that extends the
    Python list class. This custom class should
    print a notification message every time an item is added or removed.
    """
    def append(self, item):
        super().append(item)
        print(f"Added {[item]} to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with {len([items])} items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {[item]} from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {[index]} from the list.")
        return item
