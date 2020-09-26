def solution(s):
    answer = 0

    string = list(s)

    # substring : string[i:j]
    for i in range(len(string)):
        for j in range(len(string), i, -1):

            # substring의 길이
            if j-i <= answer:
                break

            # substring의 길이가 palindrome인지 확인
            if check_palindrome(s, i, j) is True:
                answer = j-i
                break

    return answer

# s[i:j]가 palindrome인지 확인하는 함수
def check_palindrome(s, i, j):
    l = j-i
    check = True
    h = l//2

    for k in range(h):
        if s[i+k] != s[j-k-1]:
            check = False
            break

    return check

if __name__ == "__main__":
    string = "abcdcba"
    print(solution(string))