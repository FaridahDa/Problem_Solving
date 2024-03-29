# Breath first search algorithm starts at a node on the graph and explores the neighbours nodes first before moving
# to the next level of neighbours explores nodes in layers we work with queues, using it to track which node to list
# next, upon visiting a new node its added to the queue to be visited later


# WRITE A PYTHON PROGRAM FOR A BREATH FIRST SEARCH
def bfs():
    matrix = [[0, 1, 1, 0],
              [0, 0, 1, 0],
              [1, 0, 0, 1],
              [0, 0, 0, 1]]

    visited = [0, 0, 0, 0]

    queue = [0]
    visited[0] = 1
    node = queue.pop(0)
    print(node)


    while True:
        for x in range(0, len(visited)):
            if matrix[node][x] == 1 and visited[x] == 0:
                visited[x] = 1
                queue.append(x)

        if len(queue) == 0:
            break

        else:
            node = queue.pop(0)
            print(node)

if __name__ == '__main__':
    bfs()
