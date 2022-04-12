# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(K, words):
    # 여기에 코드를 작성해주세요.
    wordLen = list(map(len, words))
    print(wordLen)

    answer = 1
    pos = 0
    while len(wordLen) != 0:
        if pos == 0:
            pos += wordLen.pop(0)
        elif pos + wordLen[0] + 1 <= K:
            pos += wordLen.pop(0) + 1
        else:
            pos = 0
            answer += 1
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")