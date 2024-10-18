# 37min
# split 하는 부분에서 런타임에러가 나서 20분 낭비함
from collections import defaultdict

def solution(record):
    d = defaultdict(str)
    stack = []

    for user in record:
        user_component = user.split(" ")

        if len(user_component) == 2:
            status, id = user_component[0], user_component[1]
        else:
            status, id, nickname = user_component[0], user_component[1], user_component[2]

        if status == "Leave":
            stack.append((id, "Leave"))
        elif status == "Enter":
            d[id] = nickname
            stack.append((id, "Enter"))
        elif status == "Change":
            d[id] = nickname

    ans = []
    for s in stack:
        idx = s[0]
        if s[1] == "Leave":
            ans.append(d[idx]+"님이 나갔습니다.")
        elif s[1] == "Enter":
            ans.append(d[idx]+"님이 들어왔습니다.")

    # print(ans)
    return ans

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
solution(["Enter uid1111 A", "Leave uid1111", "Enter uid1111 B", "Enter uid123 C", "Change uid123 D", "Leave uid123"])
