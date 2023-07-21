import itertools


def find_permutations(lst):
    permutations = list(itertools.permutations(lst))

    for permutation in permutations:
        print(permutation)


numbers = [1, 2, 3]
find_permutations(numbers)
