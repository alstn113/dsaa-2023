

def get_maze_answer(maze: dict) -> list:
    rows, cols = zip(*maze.keys())
    N = max(rows)
    M = max(cols)

    stack = []
    direction = {
        'E': (0, 1),
        'W': (0, -1),
        'N': (-1, 0),
        'S': (1, 0)
    }
    visited = [[False]*(M+1) for _ in range(N+1)]

    stack.append((N, M, [(N, M)]))

    visited[N][M] = True
    optimal_path = None

    while stack:
        x, y, path = stack.pop()
        if x == 1 and y == 1:
            if optimal_path is None or len(optimal_path) > len(path):
                optimal_path = path
            continue
        for d in maze[(x, y)]:

            # 벽 = 0, 길 = 1
            if maze[(x, y)][d] == 0:
                continue

            dx, dy = direction[d]
            nx = x + dx
            ny = y + dy

            if visited[nx][ny]:
                continue

            stack.append((nx, ny, path + [(nx, ny)]))
            visited[nx][ny] = True

    return optimal_path


if __name__ == '__main__':
    maze = {(1, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
            (2, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
            (3, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
            (1, 2): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
            (2, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
            (3, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 0},
            (1, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
            (2, 3): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
            (3, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}

    print(get_maze_answer(maze))
