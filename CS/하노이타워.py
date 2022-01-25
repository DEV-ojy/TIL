tower1 = {1,2,3}
tower2 = {0,0,0}
tower3 = {0,0,0}

MOVE_MESSAGE = "{}번 원반을 {}에서 {}로 이동"


def move(N, start, destination):
    print(MOVE_MESSAGE.format(N, start, destination))


def hanoi(n, start, destination, via):
    """
    하노이의 탑 규칙에 따라 원반을 옮기고,
    옮길 때마다 원반의 시작 위치와 이동한 위치를 출력합니다.
    마지막으로 총 이동 횟수를 반환합니다.
    :params
        n: 총 원반 개수
        start: 시작 기둥
        destination: 도착 기둥
        via: 보조 기둥:
    :return count:
    """
    # 원반이 1개일 때 시작 기둥에서 도착 기둥까지 한 번에 이동
    if n <= 1:
        move(1, start, destination)
        return 1

    count = 0
    # 원반 n-1개를 시작 기둥에서 보조 기둥으로 이동
    count += hanoi(n - 1, start, via, destination)

    # 가장 큰 원반을 시작 기둥에서 도착 기둥으로 이동
    count += 1
    move(n, start, destination)

    # 원반 n-1개를 보조 기둥에서 도착 기둥으로 이동
    count += hanoi(n - 1, via, destination, start)

    return count

n = 3
start = 1
destination = 3
via = 2

total_count = hanoi(n, start, destination, via)
print('총 이동 횟수:', total_count)