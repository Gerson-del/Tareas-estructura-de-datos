import tkinter as tk
import time

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1] if not self.is_empty() else None

class Array2D:
    def __init__(self, width, height):
        self.layout = [[0 for _ in range(width)] for _ in range(height)]

    def total_rows(self):
        return len(self.layout)

    def total_columns(self):
        return len(self.layout[0])

    def get_tile(self, row, col):
        return self.layout[row][col]

    def set_tile(self, row, col, value):
        self.layout[row][col] = value


maze_setup = Array2D(6, 6)
maze_setup.layout = [
    [0, 0, 0, 0, 0, 1], 
    [0, 0, 2, 2, 0, 2],
    [0, 2, 0, 0, 0, 0],
    [0, 2, 2, 2, 0, 2],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 2, 2, 0, 5]   
]

entry_point = (0, 5)  # Valor de entrada
exit_point = (5, 5)   # valor de salida
edit_mode = "toggle_wall"
canvas_area = None
gui = None


tile_colors = {
    0: "lightyellow",  # camino
    1: "navy",         # comienzo
    2: "black",        # muro
    5: "orange",       # final
    4: "red"           # parte visitada final
}


def toggle_mode(new_mode):
    """
    Cambia el modo de edición para definir la acción que se realizará 
    al hacer clic en el laberinto (como agregar o eliminar paredes).
    """
    global edit_mode
    edit_mode = new_mode
    print(f"Mode: {edit_mode}")

def change_wall(event):
    """
    Alterna el estado de una pared en el laberinto cuando se hace clic en un cuadrado.
    Si el cuadrado es un camino, lo convierte en una pared, y viceversa.
    """
    global edit_mode
    column, row = event.x // 100, event.y // 100

    if edit_mode == "toggle_wall":
        new_value = 2 if maze_setup.get_tile(row, column) == 0 else 0
        maze_setup.set_tile(row, column, new_value)
        updated_color = tile_colors[new_value]
        canvas_area.create_rectangle(column * 100, row * 100, (column + 1) * 100, (row + 1) * 100, fill=updated_color, outline="black")

def refresh_maze():
    """
    Reinicia el laberinto a su configuración inicial, eliminando todas las paredes 
    y restaurando las posiciones de entrada y salida.
    """
    global maze_setup
    maze_setup = Array2D(6, 6)
    maze_setup.layout = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5]
    ]
    update_canvas()
    print("resetear.")

def update_canvas():
    """
    Actualiza el estado visual del laberinto en la interfaz gráfica, 
    coloreando cada celda según su valor actual.
    """
    for row in range(maze_setup.total_rows()):
        for col in range(maze_setup.total_columns()):
            tile_value = maze_setup.get_tile(row, col)
            default_color = tile_colors.get(tile_value, "lightyellow")
            canvas_area.create_rectangle(col * 100, row * 100, (col + 1) * 100, (row + 1) * 100, fill=default_color, outline="black")

def start():
    """
    Configura e inicia la interfaz gráfica para el laberinto, incluyendo los botones 
    para agregar paredes, resolver el laberinto y reiniciarlo.
    """
    global gui, canvas_area
    gui, button_frame = initialize_interface(maze_setup)

    canvas_area.bind("<Button-1>", change_wall)

    wall_button = tk.Button(button_frame, text="agregar_pared", command=lambda: toggle_mode("agregar_pared"), bg="lightblue", padx=10)
    wall_button.grid(row=0, column=0, padx=10, pady=5)

    solve_button = tk.Button(button_frame, text="resolver", command=lambda: execute_solver(maze_setup, entry_point, exit_point), bg="lightgreen", padx=10)
    solve_button.grid(row=0, column=1, padx=10, pady=5)

    reset_button = tk.Button(button_frame, text="Resetear", command=refresh_maze, bg="salmon", padx=10)
    reset_button.grid(row=0, column=2, padx=10, pady=5)

    gui.mainloop()

def execute_solver(grid, start, goal):
    """
    Implementa el algoritmo de backtracking para encontrar un camino desde la posición 
    inicial hasta la meta en el laberinto. Marca el camino encontrado y los retrocesos.
    """
    route = Stack()
    route.push(start)
    movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
    explored = set()

    while not route.is_empty():
        gui.update()
        x, y = route.top()

        if (x, y) == goal:
            canvas_area.create_rectangle(y * 100, x * 100, (y + 1) * 100, (x + 1) * 100, fill="blue", outline="black")
            print("Goal reached!")
            return True

        found_path = False

        for move in movements:
            new_x, new_y = x + move[0], y + move[1]

            if 0 <= new_x < grid.total_rows() and 0 <= new_y < grid.total_columns() and grid.get_tile(new_x, new_y) in (0, 5) and (new_x, new_y) not in explored:
                route.push((new_x, new_y))
                explored.add((new_x, new_y))
                canvas_area.create_rectangle(new_y * 100, new_x * 100, (new_y + 1) * 100, (new_x + 1) * 100, fill="blue", outline="black")
                time.sleep(0.1)
                found_path = True
                break

        if not found_path:
            back_x, back_y = route.pop()
            if grid.get_tile(back_x, back_y) not in (1, 5):
                grid.set_tile(back_x, back_y, 4)
                canvas_area.create_rectangle(back_y * 100, back_x * 100, (back_y + 1) * 100, (back_x + 1) * 100, fill="red", outline="black")
                time.sleep(0.1)

    print(" ")
    return False

def initialize_interface(grid):
    """
    Inicializa la ventana principal de la interfaz gráfica y configura el 
    área de dibujo (canvas) para mostrar el laberinto.
    """
    root_window = tk.Tk()
    root_window.title("laberinto backtracking")

    display_frame = tk.Frame(root_window)
    display_frame.pack(pady=10)

    global canvas_area
    canvas_area = tk.Canvas(display_frame, width=600, height=600, bg="lightgray", borderwidth=2, relief=tk.RAISED)
    canvas_area.pack()

    update_canvas()

    button_frame = tk.Frame(root_window)
    button_frame.pack(pady=10)

    return root_window, button_frame

if __name__ == "__main__":
    start()