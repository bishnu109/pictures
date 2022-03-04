graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
}


def depth_limited_search(start, goal, path, level, maxD):
    path.append(start)

    if start == goal:
        return path

    if level == maxD:
        return False

    for child in graph[start]:
        if depth_limited_search(child, goal, path, level + 1, maxD):
            return path
        path.pop()

    return False


if __name__ == "__main__":
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    maxD = int(input("Enter the depth limit: "))

    path = []
    res = depth_limited_search(start, goal, path, 0, maxD)

    if res:
        print("Path", path)
    else:
        print("No path available for the goal node in given depth limit")
