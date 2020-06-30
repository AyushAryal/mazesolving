def createboard():
    return([
        ["-","-","S","-","+"],
        ["+","+","+","+","+"],
        ["-","-","-","+","+"],
        ["+","-","+","+","-"],
        ["+","-","+","-","+"],
        ["+","+","+","+","E"]
        ])


def printboard(maze):
    for row in maze:
        line=""
        for col in row:
            line=line+col+"      "
        print(line)
        print("\n")

maze=createboard()
printboard(maze)