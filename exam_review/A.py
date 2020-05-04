import math
import random

DEBUG = False

def solve(num, k):
    num.sort()
    for i in range(k):
        max_v = num[-1]
        num[-1] = math.ceil(max_v/2)
        if DEBUG: print("divided:", num);
        searched = binary_search(num, num[-1])
        if searched != None:
            popped = num.pop(-1)
            num.insert(searched, popped)
            if DEBUG: print("moved:", num)
    return sum(num)

def binary_search(data, target) :
    left, right = 0, len(data)
    if DEBUG: print("target:", target);
    while left <= right:
        mid = (left + right) // 2
        if DEBUG: print("index(mid):", mid);
        if DEBUG: print("value(mid-1 mid):",data[mid-1], data[mid],
                        data[mid] == target or data[mid-1] < target < data[mid]);
        if data[mid] == target:
            return mid
        if data[mid-1] < target < data[mid]:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if DEBUG: print("Return:None");
    return None

if __name__ == '__main__':
    ARRAY = [10,20,7]
    ARRAY = [1,2,3,10, 20, 7]
    print(ARRAY)
    print("Result:", solve(ARRAY, 4))

    MAX_ARRAY = [random.randint(1,10**4) for i in range(10**5)]
    print(MAX_ARRAY)
    #print("Result:", solve(MAX_ARRAY, 10**7))
    # TODO: This implementation does not fulfill the above non-functional requirement yet.
    # Thus, NEED TO BE IMPROVED, e.g. use hash search algorithm.
    print("Result:", solve(MAX_ARRAY, 10 ** 6))
