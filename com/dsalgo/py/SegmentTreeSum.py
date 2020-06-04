from math import log2, ceil


def construct_segment_tree_util(segment_tree, arr, start, end, curr):
    if start == end:
        segment_tree[curr] = arr[start]
        return segment_tree[curr]

    mid = start + (end - start) // 2

    segment_tree[curr] = construct_segment_tree_util(segment_tree, arr, start, mid,
                                                     2 * curr + 1) + construct_segment_tree_util(segment_tree, arr,
                                                                                                 mid + 1, end,
                                                                                                 2 * curr + 2)

    return segment_tree[curr]


def construct_segment_tree(arr):
    height = ceil(log2(len(arr)))
    max_size = 2 * (2 ** height) - 1

    st = [0] * max_size
    construct_segment_tree_util(st, arr, 0, len(arr) - 1, 0)

    return st


def get_sum(st, tree_start, tree_end, curr_index, query_start, query_end):
    if query_start > tree_end or query_end < tree_start:
        return 0

    if tree_start >= query_start and tree_end <= query_end:
        return st[curr_index]

    mid = tree_start + (tree_end - tree_start) // 2

    return get_sum(st, tree_start, mid, 2 * curr_index + 1, query_start, query_end) + get_sum(st, mid + 1, tree_end,
                                                                                              2 * curr_index + 2,
                                                                                              query_start, query_end)


if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11]
    segment_tree = construct_segment_tree(array)

    print("Sum of values in given range = ", get_sum(segment_tree, 0, len(array) - 1, 0, 1, 3))
