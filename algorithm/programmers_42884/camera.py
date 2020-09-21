
def solution(routes):
    answer = 0

    # 진입 지점을 기준으로 오름차순 정렬
    routes = sorted(routes, key=lambda x:x[0])
    Cpoint = -30001

    for i in range(len(routes)):
        In, Out = routes[i]

        # 진출할 때까지 카메라를 못만나므로, 카메라를 이동
        if Cpoint > Out:
            Cpoint = Out
        # 카메라 이후에 진입 지점이 존해하는 경우, 새로운 카메라가 필요
        elif Cpoint < In:
            answer += 1
            Cpoint = Out

    return answer

if __name__ == "__main__":

    r = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

    print(solution(r))