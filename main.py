from src import game, gui, connector

if __name__ == '__main__':
    grid = game.Grid(36, 28)
    wall1 = game.Wall((5, 5), 10, 'y')
    grid.setWalls(wall1)
    print(grid)
