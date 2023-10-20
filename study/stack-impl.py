class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, first_node: "Node" = None):
        if first_node is not None:
            self.top = first_node
            self.size = 1
        else:
            self.top = None
            self.size = 0

    def push(self, new_node: "Node"):
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self) -> "Node":
        if self.is_empty():
            raise Exception("Stack is empty")

        return_value = self.top
        self.top = self.top.next
        self.size -= 1

        return return_value

    def peek(self) -> "Node":
        return self.top

    def is_empty(self) -> bool:
        return True if self.size == 0 else False

    def get_size(self) -> int:
        return self.size

    def __repr__(self):
        cur_node = self.top
        out_list = []
        while cur_node is not None:
            out_list.append(str(cur_node.data))
            cur_node = cur_node.next
        out_list = reversed(out_list)
        return "-->".join(out_list)


if __name__ == "__main__":

    # Stack 클래스를 사용하여 스택을 생성합니다.
    my_stack = Stack()

    # push 메서드를 사용하여 데이터를 스택에 추가합니다.
    my_stack.push(Node(1))
    my_stack.push(Node(2))
    my_stack.push(Node(3))

    # 스택의 크기를 얻어옵니다.
    stack_size = my_stack.get_size()
    print(f"스택의 크기: {stack_size}")  # 출력: 스택의 크기: 3

    # 스택의 top 요소를 확인합니다.
    top_element = my_stack.peek()
    print(f"스택의 top 요소: {top_element.data}")  # 출력: 스택의 top 요소: 3

    # 스택 내부를 출력합니다.
    print(my_stack)  # 출력: 3-->2-->1

    # pop 메서드를 사용하여 스택에서 요소를 제거합니다.
    popped_node = my_stack.pop()
    print(f"제거된 요소: {popped_node.data}")  # 출력: 제거된 요소: 3

    # 스택의 크기를 다시 확인합니다.
    stack_size = my_stack.get_size()
    print(f"스택의 크기: {stack_size}")  # 출력: 스택의 크기: 2

    # 스택 내부를 출력합니다.
    print(my_stack)  # 출력: 2-->1
