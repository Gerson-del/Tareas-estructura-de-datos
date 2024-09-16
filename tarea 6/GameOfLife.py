import pygame
import sys
import time

class array2d:
    def __init__(self, ren, col):
        self.row_size = ren
        self.col_size = col
        self.data = [[0 for _ in range(col)] for _ in range(ren)]

    def clear(self, dato):
        for i in range(self.row_size):
            for j in range(self.col_size):
                self.data[i][j] = dato

    def get_row_size(self):
        return self.row_size

    def get_col_size(self):
        return self.col_size

    def __str__(self):
        result = ""
        for i in range(self.row_size):
            for j in range(self.col_size):
                result += str(self.data[i][j]) + ", "
            result += "\n"
        return result

    def set_value(self, ren, col, dato):
        if 0 <= ren < self.row_size and 0 <= col < self.col_size:
            self.data[ren][col] = dato
        else:
            print("Los índices están fuera de rango")

    def get_value(self, ren, col):
        if 0 <= ren < self.row_size and 0 <= col < self.col_size:
            return self.data[ren][col] if self.data[ren][col] is not None else 0
        return 0





class GameOfLife:
    def __init__(self, rows, cols, generations):
        self.board = array2d(rows, cols)
        self.generations = generations

    def contar_vecinos(self, row, colum):
        vecinos = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),        (0, 1),
                   (1, -1), (1, 0), (1, 1)]

        count = 0
        for n in vecinos:
            new_row = row + n[0]
            new_col = colum + n[1]
            if 0 <= new_row < self.board.get_row_size() and 0 <= new_col < self.board.get_col_size():
                count += self.board.get_value(new_row, new_col)
        return count

    def jugar(self):
        for gen in range(self.generations):
            print(f"Generación {gen + 1}")
            print(self.board)
            self.next_generation()
            print()

    def next_generation(self):
        new_board = array2d(self.board.get_row_size(), self.board.get_col_size())

        for row in range(self.board.get_row_size()):
            for col in range(self.board.get_col_size()):
                alive = self.board.get_value(row, col)
                neighbors = self.contar_vecinos(row, col)

                if alive and (neighbors == 2 or neighbors == 3):
                    new_board.set_value(row, col, 1)
                elif alive and (neighbors < 2 or neighbors > 3):
                    new_board.set_value(row, col, 0)
                elif not alive and neighbors == 3:
                    new_board.set_value(row, col, 1)



        self.board = new_board

CELL_SIZE = 20  
GRID_COLOR = (200, 200, 200)  
ALIVE_COLOR = (0, 255, 0) 
DEAD_COLOR = (0, 0, 0)  
BACKGROUND_COLOR = (50, 50, 50)  

def draw_grid(screen, game):
    rows, cols = game.board.get_row_size(), game.board.get_col_size()
    for row in range(rows):
        for col in range(cols):
            color = ALIVE_COLOR if game.board.get_value(row, col) == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    pygame.init()
    rows, cols, generations = 15, 15, 20
    screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()

    # crear las instancias del juego de la vida
    game = GameOfLife(rows, cols, generations)
    game.board.set_value(1, 2, 1)
    game.board.set_value(2, 2, 1)
    game.board.set_value(3, 2, 1)

    running = True
    while running and game.generations > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibuja el juego
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen, game)
        pygame.display.flip()


        game.next_generation()
        game.generations -= 1


        time.sleep(0.5)

if __name__ == "__main__":
    main()