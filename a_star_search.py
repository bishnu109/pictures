from queue import PriorityQueue


def a_star_search(graph, heuristics, source, destination):
    pq = PriorityQueue()
    pq.put((heuristics[source], [source]))

    while not pq.empty():
        node = pq.get()
        current = node[1][-1]

        if destination in node[1]:
            print("Cost:", node[0])
            print("Path:", node[1])
            return

        for neighbour in graph[current]:
            cost = node[0] + graph[current][neighbour] - heuristics[current] + heuristics[neighbour]
            path = node[1] + [neighbour]
            pq.put((cost, path))


if __name__ == "__main__":
    graph = {
        "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
        "Zerind": {"Oradea": 71, "Arad": 75},
        "Timisoara": {"Arad": 118, "Lugoj": 111},
        "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "RimnicuVilcea": 80},
        "Oradea": {"Zerind": 71, "Sibiu": 151},
        "Lugoj": {"Timisoara": 111, "Mehadia": 70},
        "RimnicuVilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
        "Mehadia": {"Lugoj": 70, "Dobreta": 75},
        "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesti": 138},
        "Pitesti": {"RimnicuVilcea": 97, "Craiova": 138, "Bucharest": 101},
        "Fagaras": {"Sibiu": 99, "Bucharest": 211},
        "Dobreta": {"Mehadia": 75, "Craiova": 120},
        "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
        "Giurgiu": {"Bucharest": 90},
        "Urziceni": {},
    }

    heuristics = {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Dobreta": 242,
        "Eforie": 161,
        "Fagaras": 176,
        "Giurgiu": 77,
        "Hirsowa": 151,
        "Lasi": 226,
        "Lugoj": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 100,
        "RimnicuVilcea": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374,
    }

    source = input("Enter source city: ")
    destination = input("Enter destination city: ")

    print()
    a_star_search(graph, heuristics, source, destination)
    print()
