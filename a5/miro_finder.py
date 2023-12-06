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

    while stack:
        x, y, path = stack.pop()
        if x == 1 and y == 1:
            return path

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

    return None
