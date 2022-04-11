from collections import deque

# 백준 1516 개임개발
def solution():
    N = int(input())
    times = [ 99999 for _ in range(N)]
    tech = []
    candidate = []
    for i in range(N):
        lists = list(map(int, input().split(" ")))
        x = {"seq": i+1, "t" : lists[0], "need" : set(lists[1:-1]), "at":0}
        if len(x["need"]) == 0:
            candidate.append(x)
        else :
            tech.append(x)

    tech = deque(tech)
    # print("tech", tech)
    # print("candidate", candidate)

    current = 0
    building = []
    buildAll(candidate, building, 0)

    while len(building) != 0:
        next = building.pop(0)
        # print("다음 건물~ ", next)
        # 완공될 대상
        times[next["seq"]-1] = next["at"]
        current = next["at"]
        n = next["seq"]

        candidate = []
        # 완공 후 조건 삭제
        for i in reversed(range(len(tech))):
            tech[i]["need"] = tech[i]["need"] - {n}
            if len(tech[i]["need"]) == 0:
                candidate.append(tech[i])
                tech.remove(tech[i])

        # 다음 지을 건물 추가
        buildAll(candidate, building, current)

    for t in times:
        print(t)

def buildAll(candidate, building, current):
    for c in candidate:
        c["at"] = current + c["t"]
        building.append(c)
    building.sort(key=lambda x:x["t"])

    # print("짓는다", building)
