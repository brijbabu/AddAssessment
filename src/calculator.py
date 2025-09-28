import re


def add(s: str) -> int:
    return sum(list(map(int, s.split(','))))
