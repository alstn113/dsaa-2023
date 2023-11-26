import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem, QWidget
from PyQt5.QtCore import Qt


class AVLNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def _rotate_left(self, y):
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_right(self, x):
        y = x.left
        T2 = y.right

        y.right = x
        x.left = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def _insert_value(self, node, key, data):
        if not node:
            return AVLNode(key, data)

        if key < node.key:
            node.left = self._insert_value(node.left, key, data)
        else:
            node.right = self._insert_value(node.right, key, data)

        self._update_height(node)

        balance = self._balance_factor(node)

        # Left Heavy
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Right Heavy
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def insert(self, key, data):
        self.root = self._insert_value(self.root, key, data)

    def search(self, key):
        return self._search_value(self.root, key)

    def _search_value(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_value(node.left, key)
        else:
            return self._search_value(node.right, key)


def tree_widget_from_avl_tree(node, parent_item=None):
    if not node:
        return

    item = QTreeWidgetItem(parent_item or [])
    item.setText(0, str(node.key))
    item.setText(1, node.data["email"])
    item.setText(2, node.data["phone"])

    item.setExpanded(True)

    tree_widget_from_avl_tree(node.left, item)
    tree_widget_from_avl_tree(node.right, item)


class AddressBookApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("주소록 관리 시스템")
        self.setGeometry(100, 100, 800, 600)

        self.avl_tree = AVLTree()

        self.init_ui()

    def init_ui(self):
        # GUI 요소 초기화
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["이름", "이메일", "전화번호"])

        self.name_edit = QLineEdit(self)
        self.email_edit = QLineEdit(self)
        self.phone_edit = QLineEdit(self)

        self.add_button = QPushButton("추가", self)
        self.search_button = QPushButton("검색", self)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("이름:"))
        form_layout.addWidget(self.name_edit)
        form_layout.addWidget(QLabel("이메일:"))
        form_layout.addWidget(self.email_edit)
        form_layout.addWidget(QLabel("전화번호:"))
        form_layout.addWidget(self.phone_edit)
        form_layout.addWidget(self.add_button)
        form_layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(form_layout)

        layout.addWidget(container)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 이벤트 핸들러 연결
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)

    def add_contact(self):
        # 연락처 추가 기능 구현
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()

        self.avl_tree.insert(name, {"email": email, "phone": phone})

        # 화면 갱신
        self.update_tree()

    def search_contact(self):
        # 연락처 검색 기능 구현
        name = self.name_edit.text()

        result = self.avl_tree.search(name)

        if result:
            data = result.data
            email = data["email"]
            phone = data["phone"]
            print(f"Name: {name}\nEmail: {email}\nPhone: {phone}")
        else:
            print(f"Contact not found.")

    def update_tree(self):
        # 트리 위젯 업데이트
        self.tree_widget.clear()

        # AVL 트리에서 데이터를 가져와서 트리 위젯에 추가
        tree_widget_from_avl_tree(self.avl_tree.root, self.tree_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    address_book_app = AddressBookApp()
    address_book_app.show()
    sys.exit(app.exec_())
