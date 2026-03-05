# 26 동계 대학생 알고리즘 특강 사전 문제
# 차량 입출차 관리

import heapq
from typing import List

class ResultE:
    def __init__(self, success: int, locname: str = ""):
        self.success = success
        self.locname = locname

class ResultS:
    def __init__(self, cnt: int, carlist: List[str]):
        self.cnt = cnt
        self.carlist = carlist

LIMIT = 0
zones = {}
parked = {}
towed = {}
tow_heap = []

def init(N: int, M: int, L: int):
    global LIMIT, zones, parked, towed, tow_heap
    LIMIT = L
    zones = {}
    parked = {}
    towed = {}
    tow_heap = []
    for i in range(N):
        zone_char = chr(ord('A') + i)
        zones[zone_char] = list(range(M))
        heapq.heapify(zones[zone_char])

def enter(mTime: int, mCarNo: str) -> ResultE:
    process_tow(mTime)
    if mCarNo in towed:
        del towed[mCarNo]
    best_zone = None
    max_empty = -1
    for zone_char, heap in zones.items():
        if len(heap) == 0:
            continue
        if len(heap) > max_empty:
            max_empty = len(heap)
            best_zone = zone_char
    if best_zone is None:
        return ResultE(0)
    slot = heapq.heappop(zones[best_zone])
    parked[mCarNo] = {
        "enter_time": mTime,
        "zone": best_zone,
        "slot": slot
    }
    heapq.heappush(tow_heap, (mTime + LIMIT, mCarNo, mTime))
    locname = f"{best_zone}{slot:03d}"
    return ResultE(1, locname)

def pullout(mTime: int, mCarNo: str):
    process_tow(mTime)
    if mCarNo in parked:
        car = parked.pop(mCarNo)
        heapq.heappush(zones[car["zone"]], car["slot"])
        return mTime - car["enter_time"]
    if mCarNo in towed:
        info = towed.pop(mCarNo)
        parking_duration = info["tow_time"] - info["enter_time"]
        towed_duration = mTime - info["tow_time"]
        return -(parking_duration + towed_duration * 5)
    return -1

def process_tow(current_time: int):
    global parked, towed, zones, tow_heap
    while tow_heap and tow_heap[0][0] <= current_time:
        tow_time, car_no, enter_time = heapq.heappop(tow_heap)
        if car_no not in parked:
            continue
        if parked[car_no]["enter_time"] != enter_time:
            continue
        car = parked.pop(car_no)
        heapq.heappush(zones[car["zone"]], car["slot"])
        towed[car_no] = {
            "enter_time": enter_time,
            "tow_time": tow_time
        }

def search(mTime: int, mStr: str):
    process_tow(mTime)
    candidates = []
    for car_no in parked:
        if car_no.endswith(mStr):
            candidates.append((0, int(car_no[:2]), car_no[2], car_no))
    for car_no in towed:
        if car_no.endswith(mStr):
            candidates.append((1, int(car_no[:2]), car_no[2], car_no))
    candidates.sort()
    carlist = [item[3] for item in candidates[:5]]
    return ResultS(len(carlist), carlist)
