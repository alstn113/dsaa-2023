import matplotlib.pyplot as plt
from collections import deque
import json


def load_graph_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[0]['inList'], data[0]['outList'], data[0]['usernameList']


def create_graph(inList, outList, usernameList):
    graph = {}
    for username in usernameList:
        graph[username] = []

    for i in range(len(inList)):
        for source in inList[i]:
            graph[usernameList[source]].append(usernameList[i])

    for i in range(len(outList)):
        for target in outList[i]:
            if usernameList[target] not in graph[usernameList[i]]:
                graph[usernameList[i]].append(usernameList[target])

    print("그래프: ", graph)
    return graph


def bfs(graph, start_node, end_node):
    visited = set()
    queue = deque([(start_node, [start_node])])
    visited.add(start_node)

    while queue:
        print([v for v, _ in queue])
        current_node, path = queue.popleft()
        print([v for v, _ in queue])

        if current_node == end_node:
            return [v for v in path]

        for v in graph[current_node]:
            if v not in visited:
                queue.append((v, path + [v]))
                visited.add(v)

    return None


def dfs(graph, start_node, end_node):
    visited = set()
    stack = [(start_node, [start_node])]
    visited.add(start_node)

    while stack:
        print([v for v, _ in stack])
        current_node, path = stack.pop()
        print([v for v, _ in stack])

        if current_node == end_node:
            return [v for v in path]

        for v in graph[current_node]:
            if v not in visited:
                stack.append((v, path + [v]))
                visited.add(v)


def main():
    inList, outList, usernameList = load_graph_data('lib/dummy_data.json')
    # inList, outList, usernameList = load_graph_data('lib/congress_network_data.json')
    graph = create_graph(inList, outList, usernameList)

    start_node = 0
    end_node = 0

    while True:
        start_node = input("시작 노드를 입력하세요: ")
        end_node = input("종료 노드를 입력하세요: ")

        if start_node not in usernameList or end_node not in usernameList:
            print("유효하지 않은 노드입니다. 다시 입력해주세요.")
            continue

        if start_node == end_node:
            print("시작 노드와 종료 노드가 같습니다. 다시 입력해주세요.")
            continue
        print()
        break

    print("BFS 시작")
    bfs_path = bfs(graph, start_node, end_node)
    print(f"BFS 경로({start_node}->{end_node}): {bfs_path}")

    print()

    print("DFS 시작")
    dfs_path = dfs(graph, start_node, end_node)
    print(f"DFS 경로({start_node}->{end_node}): {dfs_path}")


if __name__ == "__main__":
    main()
