import random

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(start_x, start_y):
        maze[2 * start_x + 1][2 * start_y + 1] = room

        first_dirs = directions.copy()
        random.shuffle(first_dirs)
        
        stack = [(start_x, start_y, first_dirs)]
        while stack:
            curr_x, curr_y, dirs = stack[-1]

            if not dirs:
                stack.pop()
                continue

            dx, dy = dirs.pop()
            nx, ny = curr_x + dx, curr_y + dy

            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                maze[2 * curr_x + 1 + dx][2 * curr_y + 1 + dy] = room
                maze[2 * nx + 1][2 * ny + 1] = room

                next_dirs = directions.copy()
                random.shuffle(next_dirs)
                stack.append((nx, ny, next_dirs))

    dfs(0, 0)

    while True:
        i = random.randint(0, 2 * m)
        j = random.randint(0, 2 * n) 
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

def maze_solver(maze, x, y, wall=1, cheese='.', path='-'):
    solved_maze = [row.copy() for row in maze]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(start_x, start_y):
        stack = [(start_x, start_y, directions.copy())]

        while maze[stack[-1][0]][stack[-1][1]] != cheese:
            curr_x, curr_y, dirs = stack[-1]

            if not dirs:
                stack.pop()
                continue

            dx, dy = dirs.pop()
            nx, ny = curr_x + dx, curr_y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != wall:
                next_dirs = directions.copy()
                next_dirs.remove((-dx, -dy))
                stack.append((nx, ny, next_dirs))
        
        return stack

    pathway = dfs(x,y)

    for step in pathway[1:-1]:
        solved_maze[step[0]][step[1]] = path

    solved_maze[1][1] = "S"

    return solved_maze

if __name__ == '__main__':
    m, n = 10, 14

    room = ' '
    wall = 'W'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze')
    print_maze(maze)

    solved_maze = maze_solver(maze, 1, 1, wall, cheese)
    print('\nSolved Maze')
    print_maze(solved_maze)