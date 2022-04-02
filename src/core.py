from itertools import combinations, permutations

# make it more efficient
def win_condition_exist(player_set):      
    win_states = set(permutations([1,2,3])) | set(permutations([4,5,6])) \
    | set(permutations([9,7,8])) | set(permutations([1,4,7])) \
    | set(permutations([8,2,5])) | set(permutations([9,3,6])) \
    | set(permutations([1,5,9])) | set(permutations([3,5,7]))
    combo = set(combinations(player_set,3))
    return combo & win_states != set()