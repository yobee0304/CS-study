# 불량 사용자

## 1. 문제
https://programmers.co.kr/learn/courses/30/lessons/64064

## 2. 유형
* 완전 탐색
* DFS

## 3. 풀이
* 우선 주어진 각각의 banned_id 마다 가능한 user_id들을 구하는 작업을 했다.
  * ex) "fr**d" -> "fraid", "fruid"
```python
    for i in range(len(banned_id)):
        masking = banned_id[i]
        tmp = []

        for j in range(len(user_id)):
            id = user_id[j]

            # check 함수 사용
            if check(masking, id) is True:
                tmp.append(id)

        candidate.append(tmp.copy())
```
* 해당 user_id가 불량 사용자가 될 수 있는지를 확인하기 위해 check 함수를 따로 만들어 사용했다.
```python
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
```
* candidate리스트에 있는 모든 사용자 아이디들을 활용하여 DFS를 통해 모든 경우의 수를 확인한다.
```python
# solution
  dfs(candidate, 0, [], answer)
  ...
  
# dfs
def dfs(candidate, cnt, id, answer):
    if cnt == len(candidate):
        # 중복 확인을 용이하기 위한 정렬
        id = sorted(id)

        # 중복 확인
        # 가능한 경우를 answer리스트에 추가
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
```

## 4. 후기
각각의 불량 사용자 아이디마다 가능한 사용자 아이디를 구하는 것만해도 3중 for문이 사용되었다.

또한 DFS를 통해 모든 경우의 수를 확인하는 것 또한 많은 시간을 필요로 하기 때문에 처음에 걱정이 되었다.

하지만 입력 조건 자체가 "8개 이하의 아이디 리스트"였기 때문에 충분히 가능하다는 판단하에 진행했다.

처음에는 5번만 시간초과가 난 상태로 통과하지 못했는데, 중복처리의 부재 때문으로 생각했다.

추후에 문제 조건에 따라 중복처리 코드를 추가한 뒤 통과할 수 있었다.

```python
# 같은 아이디가 정답 리스트에 들어갈 수 없기 때문에 제외하는 예외문
if u_id in tmp:
    continue
```

코드 성능은 매우 부족할 수 있지만, 입력 조건등을 감안했을때는 충분히 답이 될 수 있다는 가능성을 느꼈다.

또한 이에 멈추지 않고 더 빠르게 풀 수 있는 방법을 고안해봐야겠다. (5번도 겨우 통과한 느낌이 있다...)
