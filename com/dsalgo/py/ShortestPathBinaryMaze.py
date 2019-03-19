from queue import Queue


def is_valid_position(x, y, maze_list):
    return 0 <= x < len(maze_list) and 0 <= y < len(maze_list[0]) and maze_list[x][y] == 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class BinaryMaze:
    def __init__(self, maze_list):
        self.maze_list = maze_list

    def shortest_path(self, source, dest):
        if not is_valid_position(source.x, source.y, self.maze_list) or not is_valid_position(dest.x, dest.y,
                                                                                              self.maze_list):
            raise ValueError("invalid source or destination")

        visited = [[False for _ in range(len(self.maze_list[0]))] for _ in range(len(self.maze_list))]

        queue = Queue()
        queue.put(source)
        queue.put(None)

        path_len = 0

        while not queue.empty():
            current_point = queue.get()

            if current_point is None:
                path_len += 1

            else:
                if current_point == dest:
                    return path_len

                visited[current_point.x][current_point.y] = True

                if is_valid_position(current_point.x - 1, current_point.y, self.maze_list) and not \
                        visited[current_point.x - 1][current_point.y]:
                    queue.put(Point(current_point.x - 1, current_point.y))

                if is_valid_position(current_point.x + 1, current_point.y, self.maze_list) and not \
                        visited[current_point.x + 1][current_point.y]:
                    queue.put(Point(current_point.x + 1, current_point.y))

                if is_valid_position(current_point.x, current_point.y - 1, self.maze_list) and not \
                        visited[current_point.x][
                            current_point.y - 1]:
                    queue.put(Point(current_point.x, current_point.y - 1))

                if is_valid_position(current_point.x, current_point.y + 1, self.maze_list) and not \
                        visited[current_point.x][
                            current_point.y + 1]:
                    queue.put(Point(current_point.x, current_point.y + 1))

                queue.put(None)

        return -1


binary_maze_list = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]

binary_maze = BinaryMaze(binary_maze_list)
print(binary_maze.shortest_path(Point(0, 0), Point(3, 4)))
