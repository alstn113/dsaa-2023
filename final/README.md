# # Graph with Python

학번: 201911430

이름: 김민수

학과: 컴퓨터공학과 컴퓨터공학전공

## 프로젝트 소개

- 트위터 사용자간의 관계를 시각화하고, 사용자가 시작 노드와 종료 노드를 선택하여 너비 우선 탐색 (BFS) 및 깊이 우선 탐색 (DFS) 알고리즘을 실행할 수 있는 Python 프로그램입니다.

## 참고

- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10493874/

## 실행 가이드

1. 프로그램을 실행합니다

```bash
python src/main.py
```

2. 시각화된 그래프를 볼 수 있습니다. (오래 걸림)
3. 시작 노드와 종료 노드를 선택합니다.
4. BFS, DFS 경로를 확인합니다.

## 코드 설명

- `load_graph_data` 함수는 file_path에 대한 그래프 데이터를 읽어드리고, inList, outList, usernameList를 반환합니다.

- `create_graph` 함수는 inList, outList, usernameList를 이용하여 그래프를 생성하고, 그래프를 반환합니다.

  - inList는 각 노드로 들어오는 인덱스 리스트입니다.
  - outList는 각 노드에서 나가는 인덱스 리스트입니다.
  - usernameList는 각 노드의 이름 리스트입니다.

- `bfs`함수는 그래프와 시작 노드, 종료 노드를 입력받아 BFS 경로를 반환합니다.
- `dfs`함수는 그래프와 시작 노드, 종료 노드를 입력받아 DFS 경로를 반환합니다.

- `main`함수는 다음의 기능을 합니다,
  - 그래프 데이터를 읽어들입니다.
  - 그래프를 생성합니다.
  - 그래프를 시각화합니다.
  - 시작 노드와 종료 노드를 선택합니다.
  - BFS 경로를 확인합니다.
  - DFS 경로를 확인합니다.
  - 종료합니다.
