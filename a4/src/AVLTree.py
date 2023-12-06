# 효율적인 탐색 혹은 정렬 지원
# 평균 O(log n) 시간복잡도로 검색 지원
# 데이터의 저장 용이
# 사실상 binary tree의 사용 이유


class Node:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.left: "Node" = None
        self.right: "Node" = None
        # AVL 트리에서 사용하는 추가 필드
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node: "Node"):
        if not node:
            return 0
        return node.height

    def update_height(self, node: "Node"):
        if not node:
            return
        # 노드의 높이 업데이트
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node: "Node"):
        if node is None:
            return 0
        # 노드의 균형 인수 계산
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y: "Node"):
        x = y.left
        T2 = x.right

        # 회전 연산 수행
        x.right = y
        y.left = T2

        # 회전 후 노드의 높이 업데이트
        self.update_height(y)
        self.update_height(x)

        # 회전 후 새로운 루트 노드 반환
        return x

    def rotate_left(self, x: "Node"):
        y = x.right
        T2 = y.left

        # 회전 연산 수행
        y.left = x
        x.right = T2

        # 회전 후 노드의 높이 업데이트
        self.update_height(x)
        self.update_height(y)

        # 회전 후 새로운 루트 노드 반환
        return y

    def balance(self, node: "Node"):
        if node is None:
            return node

        # 현재 노드의 높이 업데이트
        self.update_height(node)

        # 불균형 여부 확인
        balance = self.balance_factor(node)

        # Left Heavy
        if balance > 1:
            # LR 불균형인 경우 왼쪽 회전 후 오른쪽 회전
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            # LL 불균형인 경우 오른쪽 회전
            return self.rotate_right(node)

        # Right Heavy
        if balance < -1:
            # RL 불균형인 경우 오른쪽 회전 후 왼쪽 회전
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            # RR 불균형인 경우 왼쪽 회전
            return self.rotate_left(node)

        # 균형이 맞을 경우 현재 노드 반환
        return node

    def insert(self, node: "Node", name, email, phone):
        if node is None:
            # 새로운 노드 생성
            return Node(name, email, phone)

        if name < node.name:
            # 왼쪽 서브트리에 삽입
            node.left = self.insert(node.left, name, email, phone)
        elif name > node.name:
            # 오른쪽 서브트리에 삽입
            node.right = self.insert(node.right, name, email, phone)
        else:
            # 중복된 키는 무시
            return node

        # 불균형을 해결한 새로운 루트 노드 반환
        return self.balance(node)

    def insert_key(self, name, email, phone):
        # 루트에서부터 삽입 시작
        self.root = self.insert(self.root, name, email, phone)

    def delete(self, node: "Node", key):
        if node is None:
            return node, False

        deleted = False
        if key == node.name:
            deleted = True

            # Case3 삭제할 노드가 자식을 두 개 가지고 있을 경우
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child

            # Case2 삭제할 노드가 자식을 한 개 가지고 있을 경우
            elif node.left or node.right:
                node = node.left or node.right

            # Case1 삭제할 노드가 리프 노드일 경우
            else:
                node = None

        elif key < node.name:
            # 왼쪽 서브트리에서 삭제 수행
            node.left, deleted = self.delete(node.left, key)
        else:
            # 오른쪽 서브트리에서 삭제 수행
            node.right, deleted = self.delete(node.right, key)

        if node:
            # 불균형을 해결한 새로운 루트 노드 반환
            return self.balance(node), deleted
        else:
            return None, deleted

    def delete_key(self, key):
        # 루트에서부터 삭제 시작
        self.root, deleted = self.delete(self.root, key)
        return deleted

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root: "Node", key):
        if root is None or root.name == key:
            # 키를 찾거나 노드가 없으면 해당 노드 반환
            return root
        elif key < root.name:
            # 왼쪽 서브트리에서 검색
            return self._find_value(root.left, key)
        else:
            # 오른쪽 서브트리에서 검색
            return self._find_value(root.right, key)


if __name__ == "__main__":
    # 데이터 삽입 예시
    avl_tree = AVLTree()
    avl_tree.insert_key("John Doe", "john.doe@example.com", "123-456-7890")
    avl_tree.insert_key("Jane Smith", "jane.smith@example.com", "987-654-3210")
    avl_tree.insert_key(
        "Bob Johnson", "bob.johnson@example.com", "555-123-4567")

    # 데이터 검색 예시
    search_key = "Jane Smith"
    if avl_tree.find(search_key):
        print(f"{search_key} found in the AVL Tree.")
    else:
        print(f"{search_key} not found in the AVL Tree.")

    # 데이터 삭제 예시
    delete_key = "Jane Smith"
    deleted = avl_tree.delete_key(delete_key)
    if deleted:
        print(f"{delete_key} deleted from the AVL Tree.")
    else:
        print(f"{delete_key} not found in the AVL Tree.")

    # 다시 검색 (이미 삭제된 노드)
    if avl_tree.find(delete_key):
        print(f"{delete_key} found in the AVL Tree.")
    else:
        print(f"{delete_key} not found in the AVL Tree.")
