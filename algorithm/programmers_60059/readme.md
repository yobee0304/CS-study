# 자물쇠와 열쇠
## 1. 문제
https://programmers.co.kr/learn/courses/30/lessons/60059
## 2. 유형
* 완전 탐색
## 3. 풀이
자물쇠를 중앙에 두고, 열쇠의 길이 m-1만큼의 두께로 둘러 쌓여있는 배열을 선언한다. 이는 열쇠의 일부만 자물쇠에 닿는 경우를 모두 탐색하기 위함이다.
```python
zero_padding = [[0 for i in range(nz)] for i in range(nz)]
    for i in range(n):
        for j in range(n):
            zero_padding[i+m-1][j+m-1] = lock[i][j]
```

열쇠를 사용해서 배열을 완전 탐색 할때, 열쇠가 회전한 4가지 경우에 대해서도 확인해 주어야한다.


이때 4가지 경우의 열쇠를 구하는 함수를 하나 선언하여 사용하였다.
```python
def rotate(key):
    rotated_keys = []

    M = len(key)

    for k in range(4):
        tmp = [[0 for i in range(M)] for i in range(M)]
        for i in range(M):
            for j in range(M):
                tmp[j][M-i-1] = key[i][j]

        key = tmp
        rotated_keys.append(key.copy())

    return rotated_keys
```

해당 열쇠가 자물쇠에 들어 맞는지를 확인하는 함수이다.

현재 위치의 열쇠 값들을 모두 배열에 더한 뒤, 모든 값이 1일때만 True를 반환합니다.

이때, 중앙에 존재하는 원래 열쇠 범위만큼만 확인합니다.

값이 1보다 커진다면 구멍이 없는데 들어가야하는 경우이기 때문에, 이 경우 또한 제외합니다.
```python
def check_open(lock, key, start_point):
    ans = True

    lock_to_check = []
    for i in lock:
        lock_to_check.append(i.copy())

    x, y = start_point
    m, nz = len(key), len(lock_to_check)

    for i in range(m):
        for j in range(m):
            lock_to_check[i+x][j+y] += key[i][j]

    for i in range(m-1, nz-m+1):
        lock_raw = lock_to_check[i][m-1:nz-m+1]
 
        if lock_raw.count(1) < len(lock_raw):
            ans = False
            break

    return ans
```

결과적으로, 총 4개의 경우의 수에 대해서 자물쇠가 열리는지를 "check_open" 함수로 확인하며 완전탐색합니다.

"check_open"이 True를 반환한다면, 반복문을 종료하고 결과값을 반환합니다.

## 4. 후기
모든 경우의 수를 생각하여 완전탐색만 하면 되는 문제였습니다.

하지만, 모든 경우의 수를 탐색할 수 있도록 새로운 배열을 만드는 아이디어가 가장 중요했던 문제였다고 생각합니다.

그리고 열쇠를 회전시키는 부분이나, 열쇠가 자물쇠를 열 수 있는지 확인하는 부분에 대해서도 상당한 시간적 지체가 있었습니다.

앞으로 더 많은 경험을 통해, 아이디어를 빠르게 도출하고 실수없이 코딩하는 훈련을 해야할 것입니다.
