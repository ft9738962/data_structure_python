import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze: #定义迷宫数据格式
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[: -1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle') 
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5, -(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self): #绘制地图
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                print(y, x)
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate, -y+self.yTranslate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y): #海龟移动
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate, -y+self.yTranslate))
        self.t.goto(x+self.xTranslate, -y+self.yTranslate)

    def dropBreadcrumb(self, color): #标记面包屑
        self.t.dot(10, color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val #更新迷宫地图
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color) #用相应颜色的面包屑标注

    def isExit(self, row, col): #判断是否位置在迷宫外
        return (row == 0 or
            row == self.rowsInMaze-1 or
            col == 0 or
            col == self.columnsInMaze-1
        )

    def __getitem__(self, idx):
        return self.mazelist[idx]

def searchFrom(maze, startRow, startCol): #海龟探索法则
    maze.updatePosition(startRow, startCol)
    #如果遇到墙
    if maze[startRow][startCol] == OBSTACLE:
        return False
    #如果四个方向都探索失败
    if maze[startRow][startCol] == TRIED or maze[startRow][startCol] == DEAD_END:
        return False
    #发现出口
    if maze.isExit(startRow, startCol):
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startCol, TRIED)
    #不属于以上状况就递归
    found = searchFrom(maze, startRow+1, startCol) or \
        searchFrom(maze, startRow-1, startCol) or \
            searchFrom(maze, startRow, startCol-1) or \
                searchFrom(maze, startRow, startCol+1)
    if found:
        maze.updatePosition(startRow, startCol, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startCol, DEAD_END)
    return found

if __name__ == "__main__":
    myMaze = Maze('maze.txt')
    myMaze.drawMaze()
    myMaze.updatePosition(myMaze.startRow, myMaze.startCol)
    searchFrom(myMaze, myMaze.startRow, myMaze.startCol)

    
