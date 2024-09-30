# 53 min
from collections import defaultdict

def solution(players, callings):
    dic = defaultdict(int)

    for pi in range(len(players)):
        dic[players[pi]] = pi

    for calling in callings:
        dic[players[dic[calling]-1]] += 1
        dic[calling] -= 1
        # print(players[dic[calling]], players[dic[calling]+1])
        players[dic[calling]], players[dic[calling] + 1] = players[dic[calling]+1], players[dic[calling]]

    return players

solution(["mumu", "soe", "poe", "kai", "mine"],
         ["kai", "kai", "mine", "mine"])
