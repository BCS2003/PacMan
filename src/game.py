class Grid:
    def __init__(self, width: int, length: int):
        self.width, self.length = width, length
        self.__walls = {}
        self.__food = {}
        self.__ghosts = {}
        self.__pac_man = None
        self.__matrix = self.__createGrid()

    def __createGrid(self):
        __matrix = []
        for i in range(self.width):
            for j in range(self.length):
                if i == 0 or j == 0 or i == self.width - 1 or j == self.length - 1:
                    __matrix.append(1)
                else:
                    __matrix.append(0)
        return __matrix

    def setWalls(self, *walls: "Wall"):
        pass

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
    def __init__(self, start: tuple[float, float], length: int, direction: str):
        self.start = start  # starting point of the wall
        self.length = length  # length of the wall
        match direction:  # faster method than if-else
            case "x":
                self.direction = (1, 0)
            case "y":
                self.direction = (0, 1)
            case _:
                raise ValueError("Invalid parameter: direction. direction should be x or y")

    def getWallPoints(self):
        pass


class Box(Wall):
    pass
