class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


def get_next_right(root):
    current_node = root

    while current_node:
        if current_node.left:
            return current_node.left
        if current_node.right:
            return current_node.right

        current_node = current_node.nextRight

    return None


def calculate_next_right_for_level(root):
    current_node = root

    while current_node:
        if current_node.left:
            if current_node.right:
                current_node.left.nextRight = current_node.right
                current_node.right.nextRight = get_next_right(current_node.nextRight)
            else:
                current_node.left.nextRight = get_next_right(current_node.nextRight)

        elif current_node.right:
            current_node.right.nextRight = get_next_right(current_node.nextRight)

        current_node = current_node.nextRight


def calculate_next_right(root):
    if root:
        # first populate nextRight of all the right nodes at this level
        if root.nextRight:
            calculate_next_right_for_level(root.nextRight)

        if root.left:
            if root.right:
                root.left.nextRight = root.right
                root.right.nextRight = get_next_right(root.nextRight)
            else:
                root.left.nextRight = get_next_right(root.nextRight)

            calculate_next_right(root.left)

        elif root.right:
            root.right.nextRight = get_next_right(root.nextRight)
            calculate_next_right(root.right)

        else:
            calculate_next_right(get_next_right(root.nextRight))


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.right.right = Node(90)

    calculate_next_right(root)

    print("nextRight of", root.data, root.nextRight.data if root.nextRight else -1)
    print("nextRight of", root.left.data, root.left.nextRight.data if root.left.nextRight else -1)
    print("nextRight of", root.right.data, root.right.nextRight.data if root.right.nextRight else -1)
    print("nextRight of", root.left.left.data, root.left.left.nextRight.data if root.left.left.nextRight else -1)
    print("nextRight of", root.right.right.data, root.right.right.nextRight.data if root.right.right.nextRight else -1)
