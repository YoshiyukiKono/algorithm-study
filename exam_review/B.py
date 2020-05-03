import random

DEBUG = False

def solve(a):
    return solution(a)

def solution(sequence):
    size = len(sequence)

    subseq_size_holder = [1] * size
    if DEBUG: print(sequence);
    if DEBUG: print(subseq_size_holder);

    for left_edge in range(1, size):
        for j in range(0, left_edge):
            if DEBUG: print(f"{left_edge} {j} : ({sequence[left_edge]} > {sequence[j]}) ? {sequence[left_edge] > sequence[j]}",
                      f"({subseq_size_holder[left_edge]} < {subseq_size_holder[j]+1}) ? ",
                      f"{subseq_size_holder[left_edge] < subseq_size_holder[j] + 1}");
            #if sequence[left_edge] > sequence[j] and subseq_size_holder[left_edge] < subseq_size_holder[j] + 1:
            #    subseq_size_holder[left_edge] = subseq_size_holder[j] + 1
            if sequence[left_edge] > sequence[j]:
                subseq_size_holder[left_edge] = max(subseq_size_holder[left_edge], subseq_size_holder[j] + 1)
            if DEBUG: print(subseq_size_holder);
            if DEBUG: print('--');

    if DEBUG: print(f"subseq_size_holder:{subseq_size_holder}");
    max_len = 0
    for i in range(size):
        max_len = max(max_len, subseq_size_holder[i])

    return max_len


if __name__ == '__main__':
    ARRAY = [1,2,2,3,1,6]
    print(ARRAY)
    print("Result:", solve(ARRAY))

    MAX_ARRAY = [random.randint(1,1000000) for i in range(1000)]
    print(MAX_ARRAY)
    print("Result:", solve(MAX_ARRAY))
