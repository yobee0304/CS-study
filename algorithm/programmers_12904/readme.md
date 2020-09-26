# 가장 긴 팰린드롬
## 1. 문제
https://programmers.co.kr/learn/courses/30/lessons/12904

## 2. 유형
* 완전 탐색(Brute Force)

## 3. 풀이
* 주어진 문자열 s에 대해서 긴 부분 문자열부터 순서대로 완전 탐색을 진행한다.
* 부분 문자열이 현재 palindrome보다 작다면 확인할 필요가 없다.
```python
for i in range(len(string)):
     for j in range(len(string), i, -1):

        # 부분 문자열과 palindrome 비교
        # 작으면 더 이상 비교할 필요가 없다
        if j-i <= answer:
            break

        # 부분 문자열의 길이가 palindrome인지 확인
        if check_palindrome(s, i, j) is True:
            answer = j-i
            break
```

* 부분 문자열이 palindrome인지 확인하기 위해 함수 선언
```python
# 부분 문자열이 palindrome인지 확인하는 함수
def check_palindrome(s, i, j):
    l = j-i
    check = True
    h = l//2

    for k in range(h):
        if s[i+k] != s[j-k-1]:
            check = False
            break

    return check
```

## 4. 후기
문제 난이도에 비해 시간이 오래 걸린 문제다.

원인은 다음과 같다.

1. 문자열이 짧은 부분 문자열부터 확인했다.
2. 부분 문자열을 확인하거나 palindrome을 확인하기 위해 '슬라이싱'을 활용했다.
3. palindrome을 확인하는 과정에서 reversed를 활용했다.

이를 개선하기 위해
1. 문자열이 긴 부분 문자열부터 확인하여, 더 짧은 문자열은 확인하지 않았다.
2. 슬라이싱대신 시작과 끝 부분의 인덱스를 잡아서 확인했다.
3. reverse대신 for문으로 직접 인덱스로 확인했다.

palindrome을 확인하는 함수를 따로 선언하지 않으면 속도거 더 개선된다는 의견을 봤지만, 고치지 않아도 시간안에 들어왔기 때문에 고치지 않았다.

슬라이싱을 활용하여 간단하게 구현할 수 있지만, 속도면에서 부족함이 있음을 인지하지 못한 것이 가장 큰 문제점이였다.

짧은 코드도 중요하지만, 최적화의 중요성을 항상 명심해야겠다.
