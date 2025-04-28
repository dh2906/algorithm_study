import math

def find_number(index):
    g = math.ceil((-1 + math.sqrt(1 + 4 * index)) / 2)
    cumulative = g * (g + 1)  # g번째까지 누적 숫자 수

    # g-1번째 그룹까지 누적 숫자
    prev_cumulative = (g-1) * g if g > 1 else 0

    # 그룹 내부에서 몇 번째인지
    position_in_group = index - prev_cumulative

    # 그룹 시작 숫자
    start_number = (g - 1) * 2 + 1

    if position_in_group <= g:
        return start_number
    else:
        return start_number + 1

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    print(find_number(y - x))