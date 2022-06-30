import maze_astar as astar
import maze_puzzle as mp
import time

print("-----------------------------------")
print("             MAZE GAME             ")
print("-----------------------------------")

while True:

    print("\n\nWYBIERZ OPCJE: ")
    print("0. EXIT")
    print("1. DZIALANIE PROGRAMU")

    wybor = int(input("Wybor: "))
    print("\n\n\n")
    if wybor == 0:
        exit(0)
    elif wybor == 1:
        x = int(input("Podaj wymiary Labiryntu - x: "))
        y = int(input("Podaj wymiary Labiryntu - y: "))
        print("")

        maze_game_main = mp.MazePuzzle(x, y)

        print("-------------------------A*------------------------")
        start = time.time()
        astar.start_astar(maze_game_main, x, y)
        end = time.time()
        print("\nTIME:")
        print(end-start)

