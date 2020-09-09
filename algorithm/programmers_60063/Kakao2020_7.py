def solution(board):
    answer = 0
    visited = []
    bfs = [[[0,0], [0,1]]]
    n = len(board)

    cnt = 0
    while True:
        b = len(bfs)

        # 1초 동안 진행하기 위해 큐의 길이만큼만 실행
        for i in range(b):
            dron = bfs[0]
            bfs.pop(0)

            # 드론이 목표지점에 도달했다면
            if [n-1, n-1] in dron:
                answer = cnt
                break

            # 이미 방문한 곳의 드론이라면 더 이상 진행하지 않음
            if dron in visited:
                continue
            else:
                dy1, dx1 = dron[0]
                dy2, dx2 = dron[1]

                visited.append(dron)

                # 오른쪽 이동
                if dx1 + 1 < n and dx2 + 1 < n and board[dy1][dx1 + 1] == 0 and board[dy2][dx2 + 1] == 0:
                    bfs.append([[dy1, dx1 + 1], [dy2, dx2 + 1]])
                # 아래로 이동
                if dy1 + 1 < n and dy2 + 1 < n and board[dy1 + 1][dx1] == 0 and board[dy2 + 1][dx2] == 0:
                    bfs.append([[dy1+1, dx1], [dy2+1, dx2]])
                # 왼쪽 이동
                if dx1 - 1 >= 0 and dx2 - 1 >= 0 and board[dy1][dx1 - 1] == 0 and board[dy2][dx2 - 1] == 0:
                    bfs.append([[dy1, dx1-1], [dy2, dx2-1]])
                # 위로 이동
                if dy1 - 1 >= 0 and dy2 - 1 >= 0 and board[dy1 - 1][dx1] == 0 and board[dy2 - 1][dx2] == 0:
                    bfs.append([[dy1-1, dx1], [dy2-1, dx2]])

                # 가로
                if dy1 == dy2:
                    # 1번을 기준으로
                    if dy1 - 1 >= 0 and dx1 + 1 < n and board[dy1 - 1][dx1 + 1] == 0 and board[dy1 - 1][dx1] == 0:
                        bfs.append([[dy1 - 1, dx1], [dy1, dx1]])
                    if dy1 + 1 < n and dx1 + 1 < n and board[dy1 + 1][dx1 + 1] == 0 and board[dy1 + 1][dx1] == 0:
                        bfs.append([[dy1, dx1], [dy1 + 1, dx1]])
                    # 2번을 기준으로
                    if dy2 - 1 >= 0 and dx2 - 1 >= 0 and board[dy2 - 1][dx2 - 1] == 0 and board[dy2 - 1][dx2] == 0:
                        bfs.append([[dy2 - 1, dx2], [dy2, dx2]])
                    if dy2 + 1 < n and dx2 - 1 >= 0 and board[dy2 + 1][dx2 - 1] == 0 and board[dy2 + 1][dx2] == 0:
                        bfs.append([[dy2, dx2], [dy2 + 1, dx2]])
                # 세로
                elif dx1 == dx2:
                    # 1번을 기준으로
                    if dy1 + 1 < n and dx1 + 1 < n and board[dy1 + 1][dx1 + 1] == 0 and board[dy1][dx1 + 1] == 0:
                        bfs.append([[dy1, dx1], [dy1, dx1 + 1]])
                    if dy1 + 1 < n and dx1 - 1 >= 0 and board[dy1 + 1][dx1 - 1] == 0 and board[dy1][dx1 - 1] == 0:
                        bfs.append([[dy1, dx1 - 1], [dy1, dx1]])
                    # 2번을 기준으로
                    if dy2 - 1 >= 0 and dx2 + 1 < n and board[dy2 - 1][dx2 + 1] == 0 and board[dy2][dx2 + 1] == 0:
                        bfs.append([[dy2, dx2], [dy2, dx2 + 1]])
                    if dy2 - 1 >= 0 and dx2 - 1 >= 0 and board[dy2 - 1][dx2 - 1] == 0 and board[dy2][dx2 - 1] == 0:
                        bfs.append([[dy2, dx2 - 1], [dy2, dx2]])

        if answer > 0:
            break

        cnt += 1

    return answer

if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],
             [0, 0, 0, 1, 0],
             [0, 1, 0, 1, 1],
             [1, 1, 0, 0, 1],
             [0, 0, 0, 0, 0]]

    # board = [[0,0,0], [0,0,0], [0,0,0]]

    print(solution(board))