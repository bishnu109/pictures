from math import ceil, log2


def minimax(tree, depth):
    is_maximizing = bool(depth % 2)

    for _ in range(depth):
        tree = [(max(a, b) if is_maximizing else min(a, b)) for a, b in zip(tree[::2], tree[1::2])]
        is_maximizing = not is_maximizing

    return tree[0]


if __name__ == "__main__":
    tree = list(map(int, input("Enter tree: ").split()))
    depth = ceil(log2(len(tree)))
    print(minimax(tree, depth))
