import random

DEBUG = False

def solve(collection, d):
    i = 1
    new_cards = []
    if DEBUG: print("Start from:", d);
    while d > 0:
        if DEBUG: print("card:", i);
        if (len(collection) > 0):
            if (collection[0] == i) :
                if DEBUG: print("card: In Collection");
                _ = collection.pop(0)
                i += 1
                continue
        if DEBUG: print("card: NOT In Collection")
        if d >= i:
            new_cards.append(i)
            d -= i
            i += 1
            if DEBUG: print("BUY - Left:", d);
        else:
            if DEBUG: print("Can NOT Buy. End");
            break

    return new_cards


if __name__ == '__main__':
    ARRAY = [1,3,4]
    print(ARRAY)
    print("Result:", solve(ARRAY, 7))

    MAX_ARRAY = [random.randint(1,10**9) for i in range(10**5)]
    D = 10**9

    print("D:",D)
    print("MAX_ARRAY Length:", len(MAX_ARRAY))
    print("MAX_ARRAY[:100]:",MAX_ARRAY[:100])

    result = solve(MAX_ARRAY, D)
    print("Result:", solve(MAX_ARRAY, D))
    print("Result Sum:", sum(result))
    print("Result Sum Check:", len(result) < D)
