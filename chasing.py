from collections import deque

# 0 < n < 100000
# 0 < k < 100000


def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return

        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v]+1
                q.append(next_step)

MAX = 10001
N, K = map(int, input().split())
time = [0]*MAX
bfs()