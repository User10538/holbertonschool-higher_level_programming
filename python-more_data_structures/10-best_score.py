#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_score = float('-inf')

    for key, score in a_dictionary.items():
        if score > best_score:
            best_score = score
            best_key = key

    return best_key
