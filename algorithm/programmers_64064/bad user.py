def solution(user_id, banned_id):
    answer = []
    candidate = []

    # 불량 사용자 아이디가 될 수 있는 아이디들을 모두 구한다
    for i in range(len(banned_id)):
        masking = banned_id[i]
        tmp = []

        for j in range(len(user_id)):
            id = user_id[j]

            if check(masking, id) is True:
                tmp.append(id)

        candidate.append(tmp.copy())

    # 불량 사용자 아이디들을 가지고 모든 경우의 수를 확인
    dfs(candidate, 0, [], answer)

    return len(answer)

# 사용자 아이디가 불량 아이디가 될 수 있는지 확인하는 함수
def check(masking_id, user_id):
    ch = True

    if len(masking_id) == len(user_id):
        for k in range(len(masking_id)):
            if masking_id[k] != '*' and masking_id[k] != user_id[k]:
                ch = False
                break
    else:
        ch = False

    return ch

# 모든 경우의 수를 확인하는 재귀 함수
def dfs(candidate, cnt, id, answer):
    if cnt == len(candidate):
        id = sorted(id)

        # 중복 확인
        if not id in answer:
            answer.append(id.copy())

        return

    L = len(candidate[cnt])

    for i in range(L):
        tmp = id.copy()
        u_id = candidate[cnt][i]

        # 이미 정답 리스트에 있는 사용자 아이디는 포함될 수 없으므로 확인
        if u_id in tmp:
            continue
        else:
            tmp.append(u_id)

        dfs(candidate, cnt+1, tmp.copy(), answer)

if __name__ == "__main__":
    u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    b = ["fr*d*", "*rodo", "******", "******"]

    print(solution(u, b))