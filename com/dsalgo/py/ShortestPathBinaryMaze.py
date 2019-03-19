def is_invalid_position(point, list):
    return point.x < 0 or point.x >= len(list) or point.y < 0 or point.y >= len(list[0])


def get_shortest_of(path1, path2, path3, path4):
    shortest_path = path1

    if shortest_path is None or path2 is not None and len(path2) < len(shortest_path):
        shortest_path = path2

    if shortest_path is None or path3 is not None and len(path3) < len(shortest_path):
        shortest_path = path3

    if shortest_path is None or path4 is not None and len(path4) < len(shortest_path):
        shortest_path = path4

    return shortest_path


class BinaryMaze:
    def __init__(self, list):
        self.list = list

    def shortest_path(self, source, dest):

        if is_invalid_position(source, list) or is_invalid_position(dest, list):
            raise ValueError("invalid source or destination")

        if self.list[dest.x][dest.y] != 1:
            raise ValueError("invalid destination")

        path_to_dest = [[None for x in len(self.list[0])] for y in len(self.list)]

        return self.__shortest_path(source, dest, path_to_dest)

    def __shortest_path(self, source, dest, path_to_dest):

        if is_invalid_position(source, self.list) or self.list[source.x][source.y] != 1:
            return None

        if path_to_dest[source.x][source.y] is not None:
            return path_to_dest[source.x][source.y]

        if source.x == dest.x and source.y == dest.y:
            path_to_dest[source.x][source.y] = [source]
            return path_to_dest[source.x][source.y]

        shortest_path_from_current_position = get_shortest_of(
            self.__shortest_path(Point(source.x - 1, source.y), dest, path_to_dest),
            self.__shortest_path(Point(source.x + 1, source.y), dest, path_to_dest),
            self.__shortest_path(Point(source.x, source.y - 1), dest, path_to_dest),
            self.__shortest_path(Point(source.x, source.y + 1), dest, path_to_dest))

        if shortest_path_from_current_position is None:
            return None

        return path_to_dest[source.x][source.y]=[source] + shortest_path_from_current_position
