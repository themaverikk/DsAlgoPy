import collections


def sorted(words):
    graph = [[0 for i in range(3)] for i in range(3)]

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            small, big = get_pair(words[i], words[j])

            if small is not None and big is not None:
                graph[small][big] = 1

    queue = collections.deque()

    indegree = [0 for i in range(len(graph))]

    for i in range(len(graph)):

        for j in range(len(graph[0])):
            if graph[j][i] == 1:
                indegree[i] += 1

        if indegree[i] == 0:
            queue.append(i)

    while queue:
        element = queue.popleft()
        print("{} ->".format(chr(element + ord('a'))), end='')

        for i in range(len(graph)):
            if graph[element][i] == 1:
                indegree[i] -= 1

                if indegree[i] == 0:
                    queue.append(i)


def get_pair(w1, w2):
    for i in range(min(len(w1), len(w2))):
        if w1[i] != w2[i]:
            return ord(w1[i]) - ord('a'), ord(w2[i]) - ord('a')


words = ("caa", "aaa", "aab")
sorted(words)
