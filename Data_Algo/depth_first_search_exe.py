# straight into the graph without regards for the edge it takes a
# backtracks when it needs to get to nodes it hasn't counted

# WRITE A PYTHON PROGRAM FOR A GRAPH USING DEPTH FIRST SEARCH ALGORITHM

ad_max = [
    # 0 1 2 3 4 5 - this is the graph
    [0, 1, 1, 1, 0, 0],  # 0
    [1, 0, 0, 0, 1, 1], #1
    [1, 0, 0, 0, 0, 5], #2,
    [1, 0, 0, 0, 0, 0], #3,
    [0, 1, 0, 0, 0, 0], #4
    [0, 1, 1, 0, 0, 0] #5
]

visited = [0, 0, 0 , 0, 0 , 0 , 0]
ans = []
stack = []


def stack_display():
    for val in stack:
        print(val, end='|')
    print()

def dfs(n):
    if visited[n] != 0:
        return

    else:
        visited[n] = 1
        stack.append(n)
        stack_display()
        num = 0
        for relation in ad_max[n]:
            if relation !=0:
                dfs(num)
            num +=1
        ans.append(n)
        stack.pop()
        stack_display()

src_node = int(input("enter a starting node: ")) # the starting node
dfs(src_node)

