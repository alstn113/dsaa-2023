from typing import List

class FileSortService:
    def __init__(self):
        pass

    def bubble_sort(self, data: List[int]) -> List[int]:
        history = [data[:]]  # 초기 데이터를 히스토리에 추가
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    history.append(data[:])  # 변경된 데이터를 히스토리에 추가
        return data, history

    def selection_sort(self, data: List[int]) -> List[int]:
        history = [data[:]]
        for i in range(len(data)):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
            history.append(data[:])
        return data, history

    def insertion_sort(self, data: List[int]) -> List[int]:
        history = [data[:]]
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            history.append(data[:])
        return data, history

    def merge_sort(self, data: List[int]) -> List[int]:
        # 병합 정렬은 분할 정복 알고리즘으로 이루어져 히스토리를 저장하기 복잡할 수 있음
        # 해당 부분은 병합 정렬의 핵심 알고리즘을 포함하여 구현해야 함
        pass

    def quick_sort(self, data: List[int]) -> List[int]:
        # 퀵 정렬도 히스토리를 추가하는데 복잡할 수 있음
        # 해당 부분은 퀵 정렬의 핵심 알고리즘을 포함하여 구현해야 함
        pass

# 사용 예시
if __name__ == "__main__":
    file_sort_service = FileSortService()

    data = [64, 25, 12, 22, 11]

    # 각 정렬 알고리즘 테스트
    sorted_data, history = file_sort_service.bubble_sort(data.copy())
    print("Bubble Sort 결과:", sorted_data)
    print("Bubble Sort 히스토리:", history)

    sorted_data, history = file_sort_service.selection_sort(data.copy())
    print("Selection Sort 결과:", sorted_data)
    print("Selection Sort 히스토리:", history)

    sorted_data, history = file_sort_service.insertion_sort(data.copy())
    print("Insertion Sort 결과:", sorted_data)
    print("Insertion Sort 히스토리:", history)
