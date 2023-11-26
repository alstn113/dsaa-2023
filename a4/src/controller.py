# 효율적인 탐색 혹은 정렬 지원
# 평균 O(log n) 시간복잡도로 검색 지원
# 데이터의 저장 용이
# 사실상 binary tree의 사용 이유


class Node:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.left = None
        self.right = None

# Binary Search Tree
class BST:
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



class TreeController:        
    pass

if __name__ == "__main__":
    # 예제로 BST를 사용해보기
    bst = BST()
    bst.insert("John Doe", "john.doe@example.com", "123-456-7890")
    bst.insert("Jane Smith", "jane.smith@example.com", "987-654-3210")
    bst.insert("Bob Johnson", "bob.johnson@example.com", "555-123-4567")