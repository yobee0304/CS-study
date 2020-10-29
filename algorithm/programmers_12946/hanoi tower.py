import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = []
    dfs(n, 1, 2, 3, answer)

    return answer

def dfs(n, start, by, dest, answer):
    # 옮기는 원반이 1개면 바로 옮겨도 된다
    if n == 1:
        answer.append([start, dest])
    else:
        # 1. start에서 by로 1개를 제외한 나머지 원반 옮기기
        dfs(n-1, start, dest, by, answer)
        # 2. 1개 남은 원반을 dest로 옮기기
        answer.append([start, dest])
        # 3. by에 옮겨놨던 n-1개의 원반을 dest로 옮기기
        dfs(n-1, by, start, dest, answer)

if __name__ == "__main__":
    n = 2
    print(solution(n))