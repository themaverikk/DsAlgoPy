class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def construct_tournament_tree(arr):
    level = []
    i = 0

    while i < len(arr):
        left = Node(arr[i])

        if i < len(arr) - 1:
            right = Node(arr[i + 1])
            min_data = min(left.data, right.data)
            root = Node(min_data, left, right)
            level.append(root)

        else:
            level.append(left)

        i += 2

    while len(level) > 1:
        temp = level
        level = []

        while temp:
            right = temp.pop(-1)
            left = temp.pop(-1)
            min_data = min(left.data, right.data)
            root = Node(min_data, left, right)
            level.append(root)

    return level.pop()


def find_second_min(root):
    second_min = root.data

    while root.left and root.right:
        root = root.left if root == root.right else root.right
        second_min = max(second_min, root.data)

    return second_min


if __name__ == "__main__":
    arr = [61, 6, 100, 9, 10, 12, 17]
    root = construct_tournament_tree(arr)
    second_min = find_second_min(root)
    print(second_min)
