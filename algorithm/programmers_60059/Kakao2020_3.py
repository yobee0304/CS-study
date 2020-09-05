def solution(key, lock):
    answer = False

    m, n = len(key), len(lock)
    nz = (m-1)*2 + n
    zero_padding = [[0 for i in range(nz)] for i in range(nz)]
    for i in range(n):
        for j in range(n):
            zero_padding[i+m-1][j+m-1] = lock[i][j]

    rotated_keys = rotate(key)

    # 4가지의 회전된 key를 가지고 직접 lock에 넣으면서 확인
    for rn in range(4):
        key = rotated_keys[rn]
        for i in range(nz-m+1):
            # print("befor nz:", zero_padding)
            for j in range(nz-m+1):
                check_true = check_open(zero_padding, key, [i, j])
                if check_true is True:
                    answer = True
                    break

            if check_true is True:
                break

        if check_true is True:
            break

    return answer

# key를 지정된 지점에서 넣었을때, 열리는지 확인하는 함수
def check_open(lock, key, start_point):
    ans = True

    lock_to_check = []
    for i in lock:
        lock_to_check.append(i.copy())

    x, y = start_point
    m, nz = len(key), len(lock_to_check)
    # print("m:", m, ", nz:", nz)

    # 열쇠 구멍에 key를 넣는다
    for i in range(m):
        for j in range(m):
            lock_to_check[i+x][j+y] += key[i][j]

    # 본래 lock인 부분이 모두 1인지 확인
    for i in range(m-1, nz-m+1):
        lock_raw = lock_to_check[i][m-1:nz-m+1]
        # print(lock_raw)
        if lock_raw.count(1) < len(lock_raw):
            # print(lock_raw, "is False")
            ans = False
            break

    return ans


# key를 회전한 총 4가지의 경우 반환
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

if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key, lock))
