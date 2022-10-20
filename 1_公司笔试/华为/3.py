distance = int(input())
if distance<=1000:
    print(int(distance//100))
N = int(input())
station = []
wait = []
for i in range(N):
    a, b = map(int, input().split(' '))
    station.append(a)
    wait.append(b)
max_distance = distance-station[-1]
for i in range(1,N):
    max_distance = max(max_distance, station[i]-station[i-1])
if max_distance > 1000:
    print(-1)
    exit()

hours = int(distance//100)

res = []

def back_track(dist):
    if dist<=1000:
        res.append(list(track))
    for i in station:

        track.append(nums[i])
        back_track()
        track.pop(-1)

back_track(2000)
