# 1 hour
# 1. 누적 시간을 구한다음,
# 2-1. 기본 시간 > 누적 시간이면, 기본 시간만큼만 부과
# 2-2. 기본 시간 < 누적 시간이면, 기본 시간(1회) + 단위 시간만큼 부과
# 잘짜지는 않은듯.
from collections import defaultdict
import math

def calculate(car, in_time, out_time):
    in_h, in_m = in_time.split(":")
    out_h, out_m = out_time.split(":")

    h, m = int(out_h) - int(in_h), int(out_m) - int(in_m)
    return [car, h * 60 + m]  # 차량번호, 시간

def solution(fees, records):
    ans = []

    basis_t, basis_f, unit_t, unit_f = fees[0], fees[1], fees[2], fees[3]

    in_dic = defaultdict(str)
    out_dic = defaultdict(bool)
    acc = []

    for record in records:
        time, car, inout = record.split()
        # 입차
        if in_dic[car] == "" and inout == "IN":
            in_dic[car] = time
            out_dic[car] = False
            acc.append([car, 0])
        # 출차
        if in_dic[car] != "" and inout == "OUT":
            acc.append(calculate(car, in_dic[car], time))
            in_dic[car] = ""
            out_dic[car] = True

    # 입차 O, 출차 X
    for car, _ in acc:
        if out_dic[car] == False:
            acc.append(calculate(car, in_dic[car], "23:59"))
            in_dic[car] = ""
            out_dic[car] = True

    acc.append(["99999", 0])  # 더미
    acc.sort()

    target_car, target_time = "", 0
    # 시간 누적 계산
    for car, time in acc:
        if target_car == "" and target_time == 0:  # 처음 집계
            target_car, target_time = car, time
        elif target_car == car:
            target_time += time
        else:
            if target_time <= basis_t:
                ans.append(basis_f)
            else:
                ans.append(basis_f + math.ceil((target_time - basis_t) / unit_t) * unit_f)
            target_car, target_time = car, time
    return ans