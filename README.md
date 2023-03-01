# Maze-Solver
This program solves mazes by finding the shortest path from the start point to the end point, subject to a limit on the number of steps. The maze is read in from a file, with ^ representing the start point, E representing the end point, and # representing walls. The program can handle multiple start and end points, and will find the shortest path that covers all of them. The shortest path found is then output to the console, with the path marked by dots (.).

How to Use:
The program provides a simple command line interface. When you run the program, you will be presented with a menu:

Menu
----
1. Find path through maze
2. Quit program

Enter 1 to find a path through a maze, or 2 to quit the program.

If you choose to find a path through a maze, you will be prompted to enter the name of the file containing the maze. The file should be a text file, with ^ representing the start point, E representing the end point, and # representing walls. 

Examples of mazes can be found from this repository, named maze1.txt and maze2.txt.

Once you have entered the name of the maze file, the program will attempt to find a path through the maze. If there are multiple start and end points, the program will find the shortest path that covers all of them. The shortest path found is then output to the console, with the path marked by dots (.). If no path is found, the program will print a message indicating this.


