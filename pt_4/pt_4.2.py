def find_combinations(candidates1, target1, current_combination, combinations1):
    if target == 0:
        combinations.append(current_combination)
        return

    if target < 0:
        return

    for i in range(len(candidates1)):
        new_combination = current_combination + [candidates1[i]]
        find_combinations(candidates1[i:], target1 - candidates1[i], new_combination, combinations1)


def get_combinations():
    candidates.sort()
    combinations1 = []
    find_combinations(candidates, target, [], combinations1)
    return combinations1


candidates = [2, 3, 6, 7]
target = 7
combinations = get_combinations(candidates, target1)
for combination in combinations:
    print(combination)
