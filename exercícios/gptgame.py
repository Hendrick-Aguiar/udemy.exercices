import PySimpleGUI as sg

# Define the game grid
grid = [
    "*********************",
    "*      *      *      *",
    "* ** * * * ** * * ** *",
    "*P * * * *    * * *  *",
    "* ** * * * ** * * ** *",
    "*      *      *      *",
    "*********************",
]

# Define Pac-Man's initial position
pacman_row = 3
pacman_col = 1

layout = [[sg.Text("Press arrow keys to move Pac-Man!")]]
layout.extend([[sg.Text(cell) for cell in row] for row in grid])

window = sg.Window("Pac-Man", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # Move Pac-Man
    if event in ("Up:38", "Down:40", "Left:37", "Right:39"):
        new_row = pacman_row
        new_col = pacman_col

        if event == "Up:38":
            new_row -= 1
        elif event == "Down:40":
            new_row += 1
        elif event == "Left:37":
            new_col -= 1
        elif event == "Right:39":
            new_col += 1

        # Check if the new position is valid (not a wall)
        if grid[new_row][new_col] != "*":
            # Update Pac-Man's position
            grid[pacman_row] = grid[pacman_row][:pacman_col] + " " + grid[pacman_row][pacman_col + 1:]
            pacman_row = new_row
            pacman_col = new_col
            grid[pacman_row] = grid[pacman_row][:pacman_col] + "P" + grid[pacman_row][pacman_col + 1:]

    # Update the game grid in the window
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            window[i + 1, j].update(grid[i][j])

window.close()
