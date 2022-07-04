class Grid:
    def __repr__(self):  # repr stands for represent
        string = "\n"
        for y in self.__matrix:
            for x in y:
                if x == 1: x = '|'
                else: x = 'o'
                string += f'{x} '
            string += '\n'
        return string

    def __init__(self, width: int, length: int):
        self.width, self.length = width, length
        self.__walls = {}
        self.__food = {}
        self.__ghosts = {}
        self.__pac_man = None
        self.__matrix = self.__createGrid()

    def __createGrid(self):
        """
        defining a matrix and adding 1 to the no. of rows if any condition is met
        :return:
        """
        __matrix = []
        for j in range(self.length):
            y = []
            for i in range(self.width):
                if i == 0 or j == 0 or i == self.width - 1 or j == self.length - 1:
                    y.append(1)
                else:
                    y.append(0)
            __matrix.append(y)
        return __matrix

    def setWalls(self, *walls: "Wall"):
        for wall in walls:
            for point in wall.getWallPoints():
                self.__matrix[point[1]][point[0]] = 1

    def setPacMan(self, x: float, y: float):
        pass

    def setGhosts(self, *ghosts: "Ghost"):
        pass


class PacMan:
    def __init__(self, img1: str, img2: str, x: float, y: float, vel: float):
        self.__img1, self.__img2 = img1, img2
        self.x, self.y = x, y
        self.vel = vel
        self.__dir = (-1, 0)
        self.lives = 3

    def move(self):
        pass

    def changeDir(self, newDir: tuple[int, int]):
        pass


class Ghost:
    """
    chase, frightened and transition are the states of the ghosts and the ghosts have varying properties according
    to their respective states.
    Chase: Normal ghost state, one ghost will chase after pacman by default
    Frightened: ghosts tend to move at a slightly slower speed, away from PacMan, and change appearance to dark blue
    transition: ghosts still are in the Frightened state, but are about to go back to the Chase state,
    """
    def __init__(self, img1: str, img2: str, img3: str, img4: str, x: float, y: float, vel: float):
        self.__img1, self.__img2, self.__img3, self.__img4 = img1, img2, img3, img4
        self.x, self.y = x, y
        self.vel = vel
        self.__dir = (-1, 0)
        self.states = ["chase", "frightened", "transition"]

    def AI_Process(self):
        pass

    def changeState(self, state: int):
        pass

    def move(self):
        pass

    def changeDir(self, newDir: tuple[int, int]):
        pass

    def changeImg(self, img1: str, img2: str, img3: str, img4: str):
        pass


class Food:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y


class BigBall(Food):
    pass


class Wall:
    def __init__(self, start: tuple[int, int], length: int, direction: str):
        assert direction in ("x", "y"),\
            "Invalid parameter: direction. direction should be x or y"  # makes sure direction is "x" or "y"
        self.start = start  # starting point of the wall
        self.length = length  # length of the wall
        self.direction = direction

    def getWallPoints(self):
        inc = 1
        if self.length < 0: inc = -1
        match self.direction:
            case "x":
                return [(k + self.start[0], self.start[1]) for k in range(0, self.length, inc)]
            case "y":
                return [(self.start[0], k + self.start[1]) for k in range(0, self.length, inc)]


class Box(Wall):
    pass
