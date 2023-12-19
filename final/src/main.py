import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import json


def load_graph_data(file_path):
    """
    파일을 load해서 inList, outList, usernameList를 반환하는 함수
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[0]['inList'], data[0]['outList'], data[0]['usernameList']


def create_graph(inList, outList, usernameList):
    """
    # inList: 각 노드로 들어오는 노드의 인덱스 리스트
    # outList: 각 노드에서 나가는 노드의 인덱스 리스트
    # usernameList: 각 노드의 이름 리스트
    """
    # 그래프 생성
    graph = nx.DiGraph()

    # 노드 추가
    for username in usernameList:
        graph.add_node(username)

    # inList를 이용해서 간선 추가
    for i in range(len(inList)):
        for source in inList[i]:
            graph.add_edge(usernameList[source], usernameList[i])

    # outList를 이용해서 간선 추가
    for i in range(len(outList)):
        for target in outList[i]:
            graph.add_edge(usernameList[i], usernameList[target])

    return graph


def bfs(graph, start_node, end_node):
    visited = set()
    queue = deque([(start_node, [start_node])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == end_node:
            return path

        if current_node in visited:
            continue

        visited.add(current_node)

        neighbors = list(graph.neighbors(current_node))
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None


def dfs(graph, start_node, end_node):
    visited = set()

    def dfs_recursive(node, path):
        if node == end_node:
            return path

        visited.add(node)
        neighbors = list(graph.neighbors(node))

        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = dfs_recursive(neighbor, path + [neighbor])
                if new_path:
                    return new_path

        return None

    return dfs_recursive(start_node, [start_node])


def main():
    # 데이터 로드
    inList, outList, usernameList = load_graph_data(
        'lib/congress_network_data.json')

    # 그래프 생성
    graph = create_graph(inList, outList, usernameList)

    # 그래프 시각화 - 그래프의 노드 수가 많아서 오래 걸림...
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold',
            node_size=700, node_color='skyblue', font_size=8, edge_color='gray')
    plt.show()

    # 시작 노드와 종료 노드 입력 받기
    while True:
        start_node = input("시작 노드를 입력하세요 ex) SenTomCotton : ")
        end_node = input("종료 노드를 입력하세요 ex) RepJoeWilson : ")

        # 시작 노드와 종료 노드가 유효한지 확인
        if start_node not in usernameList or end_node not in usernameList:
            print("유효하지 않은 노드입니다. 다시 입력해주세요.")
            continue

        # 시작 노드와 종료 노드가 같은지 확인
        if start_node == end_node:
            print("시작 노드와 종료 노드가 같습니다. 다시 입력해주세요.")
            continue

        # BFS 수행
        bfs_path = bfs(graph, start_node, end_node)
        print(f"BFS Path from {start_node} to {end_node}: {bfs_path}")

        # DFS 수행
        dfs_path = dfs(graph, start_node, end_node)
        print(f"DFS Path from {start_node} to {end_node}: {dfs_path}")

        break


if __name__ == "__main__":
    main()
