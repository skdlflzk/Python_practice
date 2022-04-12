# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(arr, K):
    arr.sort()
    # 여기에 코드를 작성해주세요.
    S = [10000 for _ in range(len(arr) - K + 1)]
    ans = 10000
    for i in range(0, len(arr) - K + 1):
        ans = min(ans, arr[i + K - 1] - arr[i])

    return ans


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 1, 1, 1, 1, 2]
K = 3
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")