from time_perf import time_prefomance

SEQUENCE = [i for i in range(1, 10_000_001)]


@time_prefomance
def linear_search_naive(seq, item):
    for ind, el in enumerate(seq):
        if el == item:
            return f'Found element {el}: on position {ind}'


# Sequence must be sorted.
@time_prefomance
def binary_search(seq, item):
    cp_seq = seq
    while True:
        mid = (len(cp_seq) - 1) // 2
        if item < cp_seq[mid] and mid != 0:
            cp_seq = cp_seq[:mid]
        elif item > cp_seq[mid] and mid != 0:
            cp_seq = cp_seq[mid:]
        elif item == cp_seq[mid] and mid != 0:
            return cp_seq[mid]
        else:
            return False


# Sequence must be sorted.
@time_prefomance
def binary_search2(seq, item):
    mid = (len(seq) - 1) // 2
    if item > seq[mid]:
        binary_search2(seq[mid+1:], item)
    elif item < seq[mid]:
        binary_search2(seq[:mid], item)
    else:
        print('end')
        return seq[mid]


@time_prefomance
def binary_search3(seq, item):
    if not seq or not (seq[0] <= item <= seq[-1]):
        return None

    first = 0
    last = len(seq) - 1
    while first <= last:
        midpoint = (first + last) // 2

        if item == seq[midpoint]:
            return f'Found element {seq[midpoint]}: on position {midpoint}'
        elif item > seq[midpoint]:
            first = midpoint + 1
        else:
            last = seq[midpoint] - 1
    return None
