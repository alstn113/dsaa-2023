import time


class FileSortController:
    def sort_data(self, data, selected_sort_algorithm, selected_sort_criteria, selected_sort_order):
        sorting_algorithm = None

        if selected_sort_algorithm == "Bubble Sort":
            sorting_algorithm = self.__bubble_sort
        elif selected_sort_algorithm == "Selection Sort":
            sorting_algorithm = self.__selection_sort
        elif selected_sort_algorithm == "Insertion Sort":
            sorting_algorithm = self.__insertion_sort
        elif selected_sort_algorithm == "Quick Sort":
            sorting_algorithm = self.__quick_sort
        elif selected_sort_algorithm == "Merge Sort":
            sorting_algorithm = self.__merge_sort
        else:
            raise Exception("Invalid sorting algorithm")

        data_copy = data.copy()
        history = [data_copy[:]]

        start_time = time.time()
        sorting_algorithm(data_copy, history,
                          selected_sort_criteria, selected_sort_order)
        end_time = time.time()

        elapsed_time = end_time - start_time

        return data_copy, history, elapsed_time

    def __bubble_sort(self, data, history, criteria, order):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if order == "Ascending":
                    if data[j][criteria] > data[j+1][criteria]:
                        data[j], data[j+1] = data[j+1], data[j]
                        history.append(data[:])
                else:
                    if data[j][criteria] < data[j+1][criteria]:
                        data[j], data[j+1] = data[j+1], data[j]
                        history.append(data[:])

    def __selection_sort(self, data, history, criteria, order):
        for i in range(len(data)):
            min_idx = i
            for j in range(i + 1, len(data)):
                if order == "Ascending":
                    if data[min_idx][criteria] > data[j][criteria]:
                        min_idx = j
                else:
                    if data[min_idx][criteria] < data[j][criteria]:
                        min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            history.append(data[:])

    # 정렬되어 있는 경우 한 번씩만 비교하므로 O(n)이 걸린다.

    def __insertion_sort(self, data, history, criteria, order):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            if order == "Ascending":
                while j >= 0 and key[criteria] < data[j][criteria]:
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = key
                history.append(data[:])
            else:
                while j >= 0 and key[criteria] > data[j][criteria]:
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = key
                history.append(data[:])

    # 피봇은 마지막 원소로 설정
    def __quick_sort(self, data, history, criteria, order):
        self.__quick_sort_recursive(
            data, history, criteria, order, 0, len(data) - 1)

    def __quick_sort_recursive(self, data, history, criteria, order, low, high):
        if low < high:
            partition_index = self.__partition(
                data, history, criteria, order, low, high)
            self.__quick_sort_recursive(
                data, history, criteria, order, low, partition_index - 1)
            self.__quick_sort_recursive(
                data, history, criteria, order, partition_index + 1, high)

    # 피봇을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할
    def __partition(self, data, history, criteria, order, low, high):
        # 피봇을 마지막 원소로 설정
        pivot = data[high][criteria]
        i = low - 1

        for j in range(low, high):
            if order == "Ascending" and data[j][criteria] <= pivot or order == "Descending" and data[j][criteria] >= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                history.append(data[:])

        data[i + 1], data[high] = data[high], data[i + 1]
        history.append(data[:])

        return i + 1

    def __merge_sort(self, data, history, criteria, order):
        self.__merge_sort_recursive(
            data, history, criteria, order, 0, len(data) - 1)

    def __merge_sort_recursive(self, data, history, criteria, order, low, high):
        # low=high가 되면 원소가 1개이므로 종료
        if low < high:
            mid = (low + high) // 2
            self.__merge_sort_recursive(
                data, history, criteria, order, low, mid)
            self.__merge_sort_recursive(
                data, history, criteria, order, mid + 1, high)
            self.__merge(data, history, criteria, order, low, mid, high)

    def __merge(self, data, history, criteria, order, low, mid, high):
        left = data[low:mid + 1]
        right = data[mid + 1:high + 1]

        i = j = 0
        k = low

        # left와 right를 비교하면서 data에 삽입
        while i < len(left) and j < len(right):
            if (order == "Ascending" and left[i][criteria] <= right[j][criteria]) or \
               (order == "Descending" and left[i][criteria] >= right[j][criteria]):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # 아래의 경우는 left와 right 중 하나는 모두 삽입이 끝난 경우이다.

        # left에 남은 게 있으면 삽입
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        # right에 남은 게 있으면 삽입
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

        history.append(data[:])
