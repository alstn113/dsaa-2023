# 파일 정렬 매니저

학번: 201911430

이름: 김민수

학과: 컴퓨터공학과 컴퓨터공학전공

## 프로젝트 소개

파일 정렬 매니저는 파일을 정렬하는 프로그램입니다.

## 실행 가이드

1. 프로그램을 실행합니다

```bash
python src/main.py
```

2. 정렬할 폴더를 선택합니다. 선택하지 않을 경우 랜덤한 파일 100개가 생성됩니다.

3. 정렬 알고리즘을 선택합니다.

   - bubble sort
   - selection sort
   - insertion sort
   - merge sort
   - quick sort

4. 정렬 기준을 선택합니다.

   - 이름
   - 크기
   - 생성 날짜

5. 정렬 방식을 선택합니다.

   - 오름차순
   - 내림차순

6. 결과를 확인합니다.

- 걸린 시간과 시간 복잡도가 표시됩니다.
- 정렬 과정이 콘솔에 표시됩니다.

# 정렬 알고리즘

참고: https://roytravel.tistory.com/328

- ## bubble sort

  시간 복잡도 : `O(n^2)`

  1번~n번까지 반복하면서, 인접한 두 원소를 비교하여 정렬한다.
  1번~n-1번까지 반복하면서, 인접한 두 원소를 비교하여 정렬한다.
  1번~n-2번까지 반복하면서, 인접한 두 원소를 비교하여 정렬한다.
  반복 ...

  ```py
  for i in range(n):
     for j in range(n-i-1):
        if arr[j] > arr[j+1]:
           arr[j], arr[j+1] = arr[j+1], arr[j]
  ```

- ## selection sort

  시간 복잡도 : `O(n^2)`

  1번~n번까지 반복하면서, 최소값을 찾아서 맨 앞으로 보낸다.
  2번~n번까지 반복하면서, 최소값을 찾아서 맨 앞으로 보낸다.
  3번~n번까지 반복하면서, 최소값을 찾아서 맨 앞으로 보낸다.
  반복 ...

  ```py
  for i in range(n):
     min_idx = i
     for j in range(i+1, n):
        if arr[min_idx] > arr[j]:
           min_idx = j
     arr[i], arr[min_idx] = arr[min_idx], arr[i]
  ```

- ## insertion sort

  시간 복잡도 : `O(n^2)` -> 정렬된 경우는 `O(n)`이다.

  2번를 뽑아서 1번과 비교하여 정렬한다.
  3번를 뽑아서 2번 1번 ...과 비교하여 정렬한다.
  4번를 뽑아서 3번 2번 1번 ...과 비교하여 정렬한다.
  반복 ...

  ```py
  for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >= 0 and key < arr[j]:
              arr[j+1] = arr[j]
              j -= 1
      arr[j+1] = key
  ```

- ## merge sort

  시간 복잡도 : `O(nlogn)`

  1. 리스트를 반으로 나눈다.
  2. 각각의 리스트를 정렬한다.
  3. 정렬된 두 리스트를 합친다.

  ```py
  def merge_sort(arr):
      if len(arr) <= 1:
          return arr
      mid = len(arr) // 2
      left = merge_sort(arr[:mid])
      right = merge_sort(arr[mid:])
      return merge(left, right)

  def merge(left, right):
      result = []
      while len(left) > 0 and len(right) > 0:
          if left[0] <= right[0]:
              result.append(left.pop(0))
          else:
              result.append(right.pop(0))
      if len(left) > 0:
          result.extend(left)
      if len(right) > 0:
          result.extend(right)
      return result
  ```

- ## quick sort

  시간 복잡도 : `O(nlogn)` -> 이미 정렬된 경우 `O(n^2)`이다.

  1. pivot을 정한다. (마지막 원소)
  2. pivot을 기준으로 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 정렬한다.
  3. 왼쪽과 오른쪽을 각각 정렬한다.

  ```py
  def quick_sort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[-1]
      left, right = [], []
      for i in range(len(arr)-1):
          if arr[i] < pivot:
              left.append(arr[i])
          else:
              right.append(arr[i])
      return quick_sort(left) + [pivot] + quick_sort(right)
  ```
