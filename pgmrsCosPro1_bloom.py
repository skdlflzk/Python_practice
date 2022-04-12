# 다음과 같이 import를 사용할 수 있습니다.
# import math
import itertools


def nextDay(garden):
    nextGarden = [[0 for _ in range(len(garden))] for _ in range(len(garden))]
    for i in range(len(garden)):
        for j in range(len(garden)):
            if garden[i][j] == 1:
                nextGarden[i][j] = 1
                if i != 0:
                    nextGarden[i - 1][j] = 1
                if i != len(garden) - 1:
                    nextGarden[i + 1][j] = 1
                if j != 0:
                    nextGarden[i][j - 1] = 1
                if j != len(garden) - 1:
                    nextGarden[i][j + 1] = 1

    return nextGarden


def allBloom(garden):
    for line in garden:
        for d in line:
            if d == 0:
                return False
    return True


def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    while not allBloom(garden):
        garden = nextDay(garden)
        answer += 1
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")