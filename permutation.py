# https://www.youtube.com/watch?v=YK78FU5Ffjw

inp = [1, 2, 3, 4, 5, 6]

def permutation(one_permute_list: list[int], final_list: list[list],
                inp: list[int], which_index_taken_list: list[bool]):
    if len(one_permute_list) == len(inp):
        final_list.append(one_permute_list[:])  # Shallow copy
        return

    for each_ind in range(len(which_index_taken_list)):
        if which_index_taken_list[each_ind]:
            continue
        which_index_taken_list[each_ind] = True
        one_permute_list.append(inp[each_ind])
        permutation(one_permute_list, final_list, inp, which_index_taken_list)
        one_permute_list.pop()  # Backtrack
        which_index_taken_list[each_ind] = False

inp = [1, 2, 3]
final_list = []
permutation([], final_list, inp, [False]*len(inp))
print(final_list)
