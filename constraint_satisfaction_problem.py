def checkEnemy(table, e):
    if len(table) == 0:
        return True

    for i in e:
        if i in table:
            return False
    return True


def csp(n, tables, enemy):
    if n <= tables:
        return True

    visited = [False for _ in range(n)]
    for i in range(n):
        for j in contentTable:
            if checkEnemy(j, enemy[i]):
                j.append(i)
                visited[i] = True
                break

        if not visited[i]:
            return False

    print(contentTable)
    return True


n = 10
tables = 3
enemy = {}
for i in range(n):
    enemy[i] = set()

e = int(input("Enter social mishap: "))
for i in range(e):
    a, b = [int(i) for i in input("Enter pair: ").split()]
    enemy[a].add(b)
    enemy[b].add(a)

contentTable = [[] for _ in range(tables)]
csp(n, tables, enemy)
