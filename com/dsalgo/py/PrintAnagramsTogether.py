def insert(root, index, word, i):
    if i < len(word):
        existing_node = root.nodes[ord(word[i]) - ord('a')]
        current_node = existing_node if existing_node else TrieNode()

        if i == len(word) - 1:
            current_node.head.append(index)
            current_node.isEnd = True

        root.nodes[ord(word[i]) - ord('a')] = current_node
        insert(current_node, index, word, i + 1)


def find_indices(root, sorted_word, i):
    if i >= len(sorted_word) or not root:
        return []

    if i == len(sorted_word) - 1:
        if root.isEnd:
            return root.head
        return []

    return find_indices(root.nodes[ord(sorted_word[i + 1]) - ord('a')], sorted_word, i + 1)


class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.head = []
        self.isEnd = False


if __name__ == "__main__":
    root = TrieNode()
    words = ["cat", "dog", "tac", "god", "act", "gdo"]

    sorted_words = set()
    for i in range(len(words)):
        sorted_word = "".join(sorted(words[i]))
        insert(root, i, sorted_word, 0)
        sorted_words.add(sorted_word)

    anagram_indices = [index for sorted_word in sorted_words for index in
                       find_indices(root.nodes[ord(sorted_word[0]) - ord('a')], sorted_word, 0)]
    print([words[i] for i in anagram_indices])
