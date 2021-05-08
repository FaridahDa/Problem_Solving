# Breath first search algorithm starts at a node on the graph and explores the neighbours nodes first before moving
# to the next level of neighbours explores nodes in layers we work with queues, using it to track which node to list
# next, upon visiting a new node its added to the queue to be visited later

def main():
    # the graphs adjacency matrix, it is used to represent a graph
    # The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph

    # 0 1 2 3 - elements in the graph
    matrix = [[0, 1, 1, 0],
              [0, 0, 1, 0],
              [1, 0, 0, 1],
              [0, 0, 0, 1]]
    # The visited array
    visited = [0, 0, 0, 0]

    # Add the start node to the queue
    # Node 0 in this case
    queue = [0]

    # set the visited value of node
    visited[0] = 1

    # Dequeue node 0
    node = queue.pop(0)
    print(node)

    while True:
        for x in range (0, len(visited)):
            # check if the route exists and that node isn't visited
            if matrix[node][x] == 1 and visited[x] == 0:
                visited[x] = 1 # visit node
                queue.append(x) # adding element to queue
        if len(queue) == 0:
            break
        else:
            #dequeue element from queue
            node = queue.pop(0)
            print(node)


if __name__ == '__main__':
    main()

