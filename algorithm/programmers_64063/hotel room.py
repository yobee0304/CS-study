import sys
sys.setrecursionlimit(10000000)

def solution(k, room_number):
    answer = []

    # 다음 방 번호를 가리키는 dict 선언
    hotel = dict()

    for target_number in room_number:
        # 해당 방이 가리키는 다음 방 번호를 answer에 추가
        empty_room = find_empty_room(hotel, target_number)
        answer.append(empty_room)

    return answer

# 해당 방이 가리키는 방 번호를 반환하는 함수
def find_empty_room(hotel, room_number):
    # 비어있는 방이라면
    # 바로 다음 방 번호를 값으로 가지는 방으로 dict에 추가
    if not room_number in hotel:
        hotel[room_number] = room_number + 1
        return room_number

    # 비어있지 않으면
    # 재귀를 통해 빈 방이 나올 때 까지 반복
    target_room_number = find_empty_room(hotel, hotel[room_number])
    hotel[room_number] = target_room_number + 1
    return target_room_number

if __name__ == "__main__":
    k = 10
    room_number = [1,3,4,1,3,1]

    print(solution(k, room_number))