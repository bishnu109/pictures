from math import inf

alpha, beta = -inf, inf
DEPTH = 4
CHILDREN = 2


def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == DEPTH:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -inf
        for i in range(CHILDREN):
            if alpha < beta:
                val = alpha_beta(depth + 1, nodeIndex * CHILDREN + i, False, values, alpha, beta)
            best = max(val, best)
            alpha = max(val, alpha)
        return best
    else:
        best = inf
        for i in range(CHILDREN):
            if alpha < beta:
                val = alpha_beta(depth + 1, nodeIndex * CHILDREN + i, True, values, alpha, beta)
            best = min(val, best)
            beta = min(val, beta)
        return best


if __name__ == "__main__":
    values = [3, 17, 2, 12, 15, 30, 25, 0, 2, 5, 3, 4, 2, 14]
    print(alpha_beta(0, 0, True, values, alpha, beta))
