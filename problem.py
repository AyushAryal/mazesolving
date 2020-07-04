from graph import Graph


def find_adjacent(board, vert_pos):
    adj = []
    x, y = vert_pos
    len_x, len_y = len(board[y]), len(board)
    if x < len_x-1 and board[y][x+1] in "+SE":
        adj.append((x+1, y))

    if y < len_y-1 and board[y+1][x] in "+SE":
        adj.append((x, y+1))

    if x != 0 and board[y][x-1] in "+SE":
        adj.append((x-1, y))

    if y != 0 and board[y-1][x] in "+SE":
        adj.append((x, y-1))
    return adj


def create_graph(board):
    vert_count = len("".join(("".join(x) for x in board)))
    graph = Graph(vert_count)
    for y, row in enumerate(board):
        for x, item in enumerate(row):
            id = x + y * len(row)

            if item in "+SE":
                for i, j in find_adjacent(board, (x, y)):
                    id_adj = i + j * len(row)
                    graph.add_uedge(id, id_adj)
    return graph


board = [
    ["+", "S", "-", "-", "-"],
    ["+", "-", "+", "+", "-"],
    ["+", "-", "-", "+", "-"],
    ["+", "+", "+", "+", "-"],
    ["-", "-", "+", "+", "+"],
    ["-", "+", "-", "E", "+"],
]


graph = create_graph(board)

start_pos = "".join(("".join(x) for x in board)).find("S")
end_pos = "".join(("".join(x) for x in board)).find("E")


path = graph.bfs(start_pos, end_pos)

for vert_id in path:
    row_length = len(board[0])
    x, y = vert_id % row_length, vert_id // row_length
    print((x,y))