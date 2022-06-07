class Grid:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.__walls = {}
        self.__food = {}
        self.__ghosts = {}
        self.__pac_man = None

        self.__createGrid()

    def __createGrid(self):
        pass

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


class BigBall(Food): pass


class Wall:
    def __init__(self, point1: tuple[float, float], point2: tuple[float, float]):
        self.point1, self.point2 = point1, point2


class Box(Wall): pass
