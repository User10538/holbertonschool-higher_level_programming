#!/usr/bin/env python3
from abc import ABC, abstractmethod 

class Animal(ABC):
    """
    Animal inherits from ABC to mark it as abstract
    has two subclass, Dog and Cat
    """
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return("Bark")

class Cat(Animal):
    def sound(self):
        return("Meow")
