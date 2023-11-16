from typing import List
import time

class FileSortService:
    def __init__(self):
        pass

    def sort_data(self, sorting_algorithm, data):
        data_copy = data.copy() 
        history = [data_copy[:]] 

        start_time = time.time() 
        sorting_algorithm(data_copy, history) 
        end_time = time.time() 

        elapsed_time = end_time - start_time 

        return data_copy, history, elapsed_time

    def bubble_sort(self, data, history):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    history.append(data[:]) 

    def selection_sort(self, data, history):
        for i in range(len(data)):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
            history.append(data[:])

    def insertion_sort(self, data, history):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            history.append(data[:])

# 사용 예시
if __name__ == "__main__":
    file_sort_service = FileSortService()

    data = [64, 25, 12, 22, 11]

    sorted_data, sort_history, elapsed_time = file_sort_service.sort_data(
        file_sort_service.bubble_sort, data
    )
    print(f"걸린 시간: {elapsed_time}초")
    print(f"정렬 과정: {sort_history}")
    print(f"정렬 결과: {sorted_data}")

    sorted_data, sort_history, elapsed_time = file_sort_service.sort_data(
        file_sort_service.selection_sort, data
    )
    print(f"걸린 시간: {elapsed_time}초")
    print(f"정렬 과정: {sort_history}")
    print(f"정렬 결과: {sorted_data}")