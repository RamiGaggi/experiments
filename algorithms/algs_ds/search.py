from time_perf import time_prefomance
from time import perf_counter
SEQUENCE = [i for i in range(1, 10_000_001)]


@time_prefomance
def linear_search_naive(seq, item):
    for i in seq:
        if i == item:
            return f'Found: {i}'


print('Linear search')
linear_search_naive(SEQUENCE, 10_000_000)


# Sequence must be sorted.
@time_prefomance
def binary_search(seq, item):
    cp_seq = seq
    while True:
        mid = len(cp_seq) // 2
        if item < cp_seq[mid] and mid != 0:
            cp_seq = cp_seq[:mid]
        elif item > cp_seq[mid] and mid != 0:
            cp_seq = cp_seq[mid:]
        elif item == cp_seq[mid] and mid != 0:
            return cp_seq[mid]
        else:
            return False


print('Binary search')
binary_search(SEQUENCE, 10_000_000)


# Sequence must be sorted.
@time_prefomance
def binary_search2(seq, item):
    if not seq:
        return False
    if not (seq[0] <= item <= seq[-1]):
        return False

    mid = len(seq) // 2
    if item > seq[mid]:
        binary_search2(seq[mid+1:], item)
    elif item < seq[mid]:
        binary_search2(seq[:mid], item)
    else:
        print('end')
        return seq[mid]
