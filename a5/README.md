> 마지막 테스트가 잘못된 것 같아서 수정 후 돌렸습니다.

> 수정된 정답: [(7, 5), (7, 4), (7, 3), (6, 3), (6, 4), (5, 4), (4, 4), (4, 3), (3, 3), (3, 4), (3, 5), (2, 5), (2, 4), (2, 3), (1, 3), (1, 2), (1, 1)]

# Miro Finder

학번: 201911430

이름: 김민수

학과: 컴퓨터공학과 컴퓨터공학전공

## 프로젝트 소개

미로를 찾아서 출구까지 가는 경로를 찾는 프로그램입니다.

## 실행 가이드

```bash
python -m unittest miro_finder_unit_test.py
```

## 코드 설명

1. N, M을 구합니다.

   ```py
   rows, cols = zip(*maze.keys())
   N = max(rows)
   M = max(cols)
   ```

2. 방문한 곳을 저장할 `visited`를 만듭니다.

   ```py
    visited = [[False]*(M+1) for _ in range(N+1)]
   ```

3. 갈 수 있는 방향에 따른 추가 x, y를 만듭니다.
   ```py
   direction = {
       'E': (0, 1),
       'W': (0, -1),
       'N': (-1, 0),
       'S': (1, 0)
   }
   ```
4. 시작 지점을 stack에 등록하고, 방문했다고 표시합니다.
5. stack이 빌 때까지 다음을 반복합니다.
   1. stack에서 지점을 하나 꺼냅니다.
   2. 현재 지점이 목적지인지 확인합니다.
   3. 현재 지점에서 갈 수 있는 방향을 확인합니다.
   4. 갈 수 있는 방향에 대해서 다음을 반복합니다.
      1. 다음 지점을 구합니다.
      2. 다음 지점을 방문했는지 확인합니다. 방문했다면 다음 방향으로 넘어갑니다.
      3. 다음 지점을 stack에 등록하고, 방문했다고 표시합니다.
