#!/usr/bin/env python3
def add(a: float, b: float) -> float:
    if not isinstance(a, float):
            raise TypeError("a must be float")
    if not isinstance(b, float):
            raise TypeError("b must be float")
    
    return a + b
    
