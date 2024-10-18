# 43 min
# A, B 사이서 선물 많이 준애가 다음달에 받는다
    # 서로간 선물 준게 동일하면, 선물지수에 따라 결정
    # 선물 지수도 동일하면 선물 주고 받지 않음
# 가장 많이 선물받는 애는 몇개를 받을까?

# friends
    # ["muzi", "ryan", "frodo", "neo"]
# gifts
    # ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
# result
    # 2

from collections import defaultdict

def solution(friends, gifts):
    d = defaultdict(lambda: defaultdict(int))
    sended = defaultdict(int)
    received = defaultdict(int)
    exp = defaultdict(int)
    ans = defaultdict(int)

    for friend_i in friends:
        for friend_j in friends:
            if not friend_i == friend_j:
                d[friend_i][friend_j] = 0

    for gift in gifts:
        sender, receiver = gift.split()
        d[sender][receiver] += 1

    for key, value in d.items():
        sended[key] += sum(value.values())
        for v_key, v_value in value.items():
            received[v_key] += v_value

    for key, value in d.items():
        exp[key] = sended[key] - received[key]

    # print(sended)
    # print(received)
    # print(exp)

    sender: object
    for sender, sended_value in d.items():
        # print(sender, sended_value)
        for receiver, received_value in sended_value.items():
            receiver_to_sender_value = d[receiver][sender]
            # print(receiver, received_value, receiver_to_sender_value)
            if received_value > receiver_to_sender_value:
                ans[sender] += 1
            elif received_value == receiver_to_sender_value and exp[sender] > exp[receiver]:
                ans[sender] += 1

    if len(ans) > 0:
        return max(ans.values())
    else:
        return 0

solution(["muzi", "ryan", "frodo", "neo"],
         ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])