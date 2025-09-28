import re


def add(s: str) -> int:
    delimiter = re.search('^//(.*)\\n', s)

    if delimiter:
        s = re.sub("^//(.*)\\n", "", s)
        s = s.replace(delimiter.groups()[0], ",")

    s = s.replace("\n", ",")

    if not s:
        return 0

    if "-" in s:
        negative_nos = re.findall('(-\\d+)', s)
        raise ValueError(f"negative numbers not allowed {','.join(negative_nos)}")

    numbers = list(map(int, s.split(',')))
    return sum(numbers)
