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
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node: "Node"):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y: "Node"):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x: "Node"):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def balance(self, node: "Node"):
        if node is None:
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Heavy
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Heavy
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, node: "Node", name, email, phone):
        if node is None:
            return Node(name, email, phone)

        if name < node.name:
            node.left = self.insert(node.left, name, email, phone)
        elif name > node.name:
            node.right = self.insert(node.right, name, email, phone)
        else:
            return node

        return self.balance(node)

    def insert_key(self, name, email, phone):
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
            node.left, deleted = self.delete(node.left, key)
        else:
            node.right, deleted = self.delete(node.right, key)

        if node:
            return self.balance(node), deleted
        else:
            return None, deleted

    def delete_key(self, key):
        self.root, deleted = self.delete(self.root, key)
        return deleted

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root: "Node", key):
        if root is None or root.name == key:
            return root
        elif key < root.name:
            return self._find_value(root.left, key)
        else:
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
