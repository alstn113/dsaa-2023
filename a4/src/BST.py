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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, name, email, phone):
        self.root = self._insert_value(self.root, name, email, phone)
        return self.root is not None

    def _insert_value(self, node: "Node", name, email, phone):
        if node is None:
            node = Node(name, email, phone)
        else:
            if name <= node.name:
                node.left = self._insert_value(node.left, name, email, phone)
            else:
                node.right = self._insert_value(node.right, name, email, phone)
        return node

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node: "Node", key):
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
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root: "Node", key):
        if root is None or root.name == key:
            return root is not None
        elif key < root.name:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)


if __name__ == "__main__":
    # 데이터 삽입 예시
    bst = BinarySearchTree()
    bst.insert("John Doe", "john.doe@example.com", "123-456-7890")
    bst.insert("Jane Smith", "jane.smith@example.com", "987-654-3210")
    bst.insert("Bob Johnson", "bob.johnson@example.com", "555-123-4567")

    # 데이터 검색 예시
    search_key = "Jane Smith"
    if bst.find(search_key):
        print(f"{search_key} found in the BST.")
    else:
        print(f"{search_key} not found in the BST.")

    # 데이터 삭제 예시
    delete_key = "Jane Smith"
    deleted = bst.delete(delete_key)
    if deleted:
        print(f"{delete_key} deleted from the BST.")
    else:
        print(f"{delete_key} not found in the BST.")

    # 다시 검색 (이미 삭제된 노드)
    if bst.find(delete_key):
        print(f"{delete_key} found in the BST.")
    else:
        print(f"{delete_key} not found in the BST.")
