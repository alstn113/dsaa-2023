from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTreeWidget, QTreeWidgetItem, QWidget, QFileDialog
import random
from AVLTree import AVLTree, Node


class MainView(QMainWindow):
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

        # 각 열의 기본 너비 설정
        self.tree_widget.setColumnWidth(0, 300)
        self.tree_widget.setColumnWidth(1, 200)
        self.tree_widget.setColumnWidth(2, 150)

        self.name_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)

        self.add_button = QPushButton("추가", self)
        self.search_button = QPushButton("검색", self)
        self.save_button = QPushButton("저장", self)
        self.load_button = QPushButton("불러오기", self)

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

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.load_button)

        container = QWidget()
        container.setLayout(vertical_layout)
        layout.addWidget(container)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 이벤트 핸들러 연결
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)
        self.save_button.clicked.connect(self.save_to_csv)
        self.load_button.clicked.connect(self.load_from_csv)

        # 초기 데이터 추가
        # for _ in range(15):
        #     name = "".join(random.choices(
        #         "abcdefghijklmnopqrstuvwxyz1234567890", k=5))
        #     email = f"{name.lower()}@gmail.com"
        #     phone = f"010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        #     self.avl_tree.insert_key(name, email, phone)

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
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()

        if self.avl_tree.find(name):
            print("[✅ 추가 결과]: 이미 존재하는 이름입니다.")
        else:
            self.avl_tree.insert_key(name, email, phone)
            print(f"[❎ 추가 결과]: {name}, {email}, {phone}")

        # 화면 갱신
        self.update_tree()

    def search_contact(self):
        # 연락처 검색 기능 구현
        name = self.find_name_input.text()

        target_node = self.avl_tree.find(name)

        if target_node:
            email = target_node.email
            phone = target_node.phone
            print(f"[🔍 검색 결과]: {name}, {email}, {phone}")
        else:
            print(f"[🔍 검색 결과]: 존재하지 않는 이름입니다.")

    def save_to_csv(self):
        # 파일 대화상자를 열어 사용자로부터 저장할 위치를 선택받습니다.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(
            self, "주소록 저장", "", "CSV Files (*.csv);;All Files (*)", options=options)

        # 사용자가 취소를 누르면 무시합니다.
        if not file_name:
            return

        # 선택된 파일에 주소록을 저장합니다.
        with open(file_name, mode='w', encoding='utf-8') as file:
            # CSV 파일에 헤더를 쓰기
            file.write("이름,이메일,전화번호\n")

            # AVL 트리를 중위 순회하며 데이터를 CSV 파일에 쓰기
            self._inorder_traversal_save(self.avl_tree.root, file)

        print(f"[💾 저장 결과]: 주소록이 {file_name}에 성공적으로 저장되었습니다.")

    def _inorder_traversal_save(self, node: "Node", file):
        if not node:
            return

        # 왼쪽 서브트리 순회
        self._inorder_traversal_save(node.left, file)

        # 노드 데이터 CSV 파일에 쓰기
        file.write(f"{node.name},{node.email},{node.phone}\n")

        # 오른쪽 서브트리 순회
        self._inorder_traversal_save(node.right, file)

    def load_from_csv(self):
        # AVL 트리 초기화
        self.avl_tree = AVLTree()

        # 파일 대화상자를 열어 사용자로부터 불러올 파일을 선택받습니다.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "주소록 불러오기", "", "CSV Files (*.csv);;All Files (*)", options=options)

        # 사용자가 취소를 누르면 무시합니다.
        if not file_name:
            return

        # 선택된 파일에서 주소록을 불러옵니다.
        with open(file_name, mode='r', encoding='utf-8') as file:
            # CSV 파일의 헤더를 무시합니다.
            file.readline()

            # CSV 파일의 데이터를 읽어서 AVL 트리에 추가합니다.
            for line in file:
                name, email, phone = line.strip().split(',')
                self.avl_tree.insert_key(name, email, phone)

        print(f"[📂 불러오기 결과]: 주소록이 {file_name}에서 성공적으로 불러와졌습니다.")

        # 화면 갱신
        self.update_tree()

    def update_tree(self):
        # 트리 위젯 업데이트
        self.tree_widget.clear()

        # AVL 트리에서 데이터를 가져와서 트리 위젯에 추가
        self.tree_widget_from_avl_tree(self.avl_tree.root, self.tree_widget)
