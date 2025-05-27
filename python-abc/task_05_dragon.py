#!/usr/bin/env python3

class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print ("The dragon roars!")

class draco(Dragon):
    def swim(self):
        return super().swim()
    def fly(self):
        return super().fly()
    def roar(self):
        return super().roar()
