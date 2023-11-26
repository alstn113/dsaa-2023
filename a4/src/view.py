from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem, QWidget
from PyQt5.QtCore import Qt
from binary_search_tree import BinarySearchTree, Node


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("주소록 관리 시스템")
        self.setGeometry(100, 100, 800, 600)

        self.avl_tree = BinarySearchTree()

        self.init_ui()

    def init_ui(self):
        # GUI 요소 초기화
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["이름", "이메일", "전화번호"])

        self.name_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)

        self.add_button = QPushButton("추가", self)
        self.search_button = QPushButton("검색", self)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)

        vertical_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("이름:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("이메일:"))
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(QLabel("전화번호:"))
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.add_button)
        vertical_layout.addLayout(form_layout)

        search_layout = QHBoxLayout()
        self.find_name_input = QLineEdit(self)
        search_layout.addWidget(QLabel("검색할 이름:"))
        search_layout.addWidget(self.find_name_input)
        search_layout.addWidget(self.search_button)
        vertical_layout.addLayout(search_layout)

        container = QWidget()
        container.setLayout(vertical_layout)

        layout.addWidget(container)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 이벤트 핸들러 연결
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)

        # 초기 데이터 추가
        self.avl_tree.insert("김민수", "minsu.kim@example.com", "010-1234-5678")
        self.avl_tree.insert("이하나", "hana.lee@example.com", "010-2345-6789")
        self.avl_tree.insert(
            "박철수", "chulsoo.park@example.com", "010-3456-7890")
        self.avl_tree.insert(
            "최영희", "younghee.choi@example.com", "010-4567-8901")
        self.avl_tree.insert("정다혜", "dahye.jung@example.com", "010-5678-9012")
        self.avl_tree.insert("김철수", "cjftn@gmail.com", "010-1234-5678")
        self.avl_tree.insert("이영희", "dudgml@gmail.com", "010-2345-6789")

        self.tree_widget_from_avl_tree(self.avl_tree.root, self.tree_widget)

    def tree_widget_from_avl_tree(self, node: "Node", parent_item=None):
        if not node:
            return

        item = QTreeWidgetItem(parent_item or [])
        item.setText(0, node.name)
        item.setText(1, node.email)
        item.setText(2, node.phone)

        item.setExpanded(True)

        self.tree_widget_from_avl_tree(node.left, item)
        self.tree_widget_from_avl_tree(node.right, item)

    def add_contact(self):
        # 연락처 추가 기능 구현
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()

        if self.avl_tree.find(name):
            print("[✅ 추가 결과]: 이미 존재하는 이름입니다.")
        else:
            self.avl_tree.insert(name, email, phone)
            print(f"[❎ 추가 결과]: {name}, {email}, {phone}")

        # 화면 갱신
        self.update_tree()

    def search_contact(self):
        # 연락처 검색 기능 구현
        name = self.name_edit.text()

        target_node = self.avl_tree.find(name)

        if target_node:
            email = target_node.email
            phone = target_node.phone
            print(f"[🔍 검색 결과]: {name}, {email}, {phone}")
        else:
            print(f"[🔍 검색 결과]: 존재하지 않는 이름입니다.")

    def update_tree(self):
        # 트리 위젯 업데이트
        self.tree_widget.clear()

        # AVL 트리에서 데이터를 가져와서 트리 위젯에 추가
        self.tree_widget_from_avl_tree(self.avl_tree.root, self.tree_widget)
