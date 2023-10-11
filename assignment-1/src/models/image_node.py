class ImageNode:
    """
    노드 클래스
    """

    def __init__(self, image_name: str,  image_path: str, created_at: int):
        self.__image_name: str = image_name
        self.__image_path: str = image_path
        self.__created_at: str = created_at

        self.__prev: 'ImageNode' = None
        self.__next: 'ImageNode' = None

    def set_prev(self, prev: 'ImageNode'):
        self.__prev = prev

    def set_next(self, next: 'ImageNode'):
        self.__next = next

    def get_prev(self) -> 'ImageNode':
        return self.__prev

    def get_next(self) -> 'ImageNode':
        return self.__next

    def get_image_name(self) -> str:
        return self.__image_name

    def get_image_path(self) -> str:
        return self.__image_path

    def get_created_at(self) -> int:
        return self.__created_at
