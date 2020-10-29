# 호텔 방 배정

## 1. 문제
https://programmers.co.kr/learn/courses/30/lessons/64063

## 2. 유형
- Recursive Function
- Union-Find

## 3. 풀이
* <Key, Value> 값이 <방 번호, 다음 방 번호> 인 dictation을 선언한다
* 입력 받은 방 번호에 의해서 차례대로 방을 채운다.
* 만약 해당 방이 이미 차있는 경우, 이후에 가장 가까운 빈 방을 찾아야 하므로 빈 방을 찾아주는 함수 선언
  * 방이 빈 방이라면
    * 해당 방 번호를 반환하고, 해당 번호의 방에 바로 다음 방 번호를 입력
  * 방이 이미 차있는 방이라면
    * 가장 가까운 빈 방을 찾기 위해 재귀를 통해 반복
    * 재귀를 진행하면서 중간의 방들도 값을 갱신 (이후에 실행 속도를 증가시키기 위해서)
    * 빈 방의 번호를 반환하고, 빈 방에 그 다음 방 번호를 입력
```python
def find_empty_room(hotel, room_number):
    # 비어있는 방이라면
    if not room_number in hotel:
        hotel[room_number] = room_number + 1
        return room_number

    # 비어있지 않으면
    target_room_number = find_empty_room(hotel, hotel[room_number])
    hotel[room_number] = target_room_number + 1
    return target_room_number
```

## 4. 후기
유니온 파인드를 통해 빈 방을 최대한 빠르게 찾아주는 것이 관건인 문제였다.

문제를 풀면서 직면한 문제들은 다음과 같다.

1. 방을 동적 자료구조로 처리하지 않고, k개만큼 선언하고 문제를 시작했다.

입력된 방의 개수는 2*10^5인 반면, k는 최대 10^12개가 될 수 있으므로 엄청난 손해를 보고 문제를 접근한 셈이다.

```python
hotel = [i for i in range(k+1)]
```

2. find_empty_rooms함수에서 재귀를 진행하면서 방 번호를 갱신하지 않았다.

빈 방을 찾으면서 값을 갱신 한다면 다음 번 실행 시간을 줄일 수 있다.

예를 들면, 1 - 3 - 5 - 7로 진행하면서 1,3,5을 7로 갱신했다면 1 - 3 - 5 - 7 - 9 진행을 1 - 7 - 9로 단축 시킬 수 있는 것이다.

3. 최대 재귀 깊이를 설정하지 않았다.

탐색 알고리즘(BFS, DFS)는 보통 재귀를 많이 사용한다.

하지만, python의 기본 재귀 깊이로는 문제를 만족하지 못하고 '런타임 에러'가 나는 경우가 종종 발생한다.

그렇기 때문에, 재귀 깊이가 깊어질 경우를 고려하여 재귀 허용 깊이를 늘려줘야 한다.

```python
import sys
sys.setrecursionlimit(10000000)
```

이 부분을 찾아보면서, python으로 알고리즘을 풀 때 주의해야 할 점을 더 확인했다. 참고하면 좋을 것 같다.

(참고 : https://dailyheumsi.tistory.com/32)
