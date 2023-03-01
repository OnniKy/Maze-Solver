def print_menu():
    """
    Prints the main menu. Gets and returns none.
    """
    print("\nMenu")
    print("----")
    print("1. Find path through maze")
    print("2. Quit program")

def get_choice():
    """
    Prompts the user for their choice and returns
    the choice as an integer.
    """
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:\
                    print("Invalid choice. Please enter a number.")

def read_maze():
    """
        Reads in the maze from the specified file. Gets none and returns maze as a list.
    """
    maze = []
    while True:
        try:
            filename = input("Enter file name: ")
            with open(filename) as f:
                for line in f:
                    maze.append(list(line.strip()))
            return maze

        except:
            print("Invalid file name. Please enter filename again.")

def write_maze(maze, path):
    """
        Writes the maze with the specified path to the console. Gets maze and path & returns none.
        Replaces the path with dots (.) in the maze.
    """
    for x, y in path:
        maze[x][y] = '.'
    out = "\n".join("".join(row) for row in maze)
    print("\n")
    print(out)
    return None

def find_start_and_end_points(maze):
    """
        Finds the start and end points in the maze.
        Returns them as (x, y) tuples or None if not found.
    """
    start_points = [(i, row.index('^')) for i, row in enumerate(maze) if '^' in row]
    end_points = [(i, row.index('E')) for i, row in enumerate(maze) if 'E' in row]

    if not start_points or not end_points:
        return None, None

    return start_points, end_points

def find_shortest_path_for_points(maze, start_points, end_points):
    """
    Finds the shortest path from any start point to any end point within the specified number of steps.
    Returns the path as a list of (x, y) tuples or None if no path was found.
    """
    shortest_path = None
    for start in start_points:
        for end in end_points:
            for max_steps in [20, 150, 200]:
                path = find_shortest_path(maze, start, max_steps)
                if path is not None and (shortest_path is None or len(path) < len(shortest_path)):
                    shortest_path = path
                    shortest_steps = max_steps

    return shortest_path, shortest_steps

def find_shortest_path(maze, start, max_steps):
    """
        Finds the shortest path from any start point to any end point within the specified number of steps.
        Returns the path as a list of (x, y) tuples or None if no path was found.
    """
    def search(x, y, steps, visited, path):
        if steps > max_steps:
            return None
        if maze[x][y] == '#':
            return None
        if maze[x][y] == 'E':
            return path + [(x, y)]
        if visited[x][y]:
            return None
        visited[x][y] = True

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze[0]):
                continue

            new_path = search(nx, ny, steps + 1, visited, path + [(x, y)])

            if new_path is not None:
                return new_path
        return None

    visited = [[False] * len(maze[0]) for _ in range(len(maze))]

    return search(start[0], start[1], 0, visited, [])

"""Main program"""
while True:
    """
    Runs the maze solving program. Displays menu options, asks user for choice. Calls methods according to choice and maze type.
    Stops program if needed.
    """
    print_menu()
    choice = get_choice()
    if choice == 1:
        maze = read_maze()
        start_points, end_points = find_start_and_end_points(maze)

        # Missing start or end point
        if start_points is None or end_points is None:
            print("Error: start or end point not found in maze.")
            continue

        # Multiple start or end points
        if len(start_points) > 1 or len(end_points) > 1:
            print("Note: multiple start or end points. Finding shortest path.")
            shortest_path, shortest_steps = find_shortest_path_for_points(maze, start_points, end_points)

            if shortest_path is not None:
                print(f"Shortest path found in {shortest_steps} steps:")
                write_maze(maze, shortest_path)
            else:
                print("Path not found.")

        # Only one start and end point
        else:
            shortest_path, shortest_steps = find_shortest_path_for_points(maze, start_points, end_points)
            if shortest_path is not None:
                print(f"Path found in {shortest_steps} steps:")
                write_maze(maze, shortest_path)
            else:
                print("Path not found.")

    # If the user chooses to quit the program, exit the loop
    elif choice == 2:
        print("Thank you for using the program.")
        break
