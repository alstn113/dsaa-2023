from service import FileSortService


class FileSortController:
    def __init__(self, file_sort_service: "FileSortService"):
        self.file_sort_service = file_sort_service
