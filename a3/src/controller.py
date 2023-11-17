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
        sorting_algorithm(data_copy, history, selected_sort_criteria, selected_sort_order) 
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

    def __insertion_sort(self, data, history, criteria, order):
        for i in range(len(data)):
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
    
    def __quick_sort(self, data, history, criteria, order):
        return

    def __merge_sort(self, data, history, criteria, order):
        return