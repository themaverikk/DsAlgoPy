n = input()

groups = list(map(int, input().split(" ")))

ga = [0 for _ in range(4)]

for i in groups:
    ga[i - 1] += 1

taxi = ga[3]

ga[0] = max(0, ga[0] - ga[2])
taxi += ga[2]

taxi += ga[1] // 2
ga[1] = ga[1] % 2

if ga[1]:
    ga[0] = max(ga[0] - 2, 0)
    taxi += 1

taxi += ga[0] // 4
taxi += (ga[0] % 4) > 0

print(taxi)
