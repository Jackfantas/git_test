# n 代表技能数, m 代表回合数, k代表连续使用技能的次数
n, m, k = map(int, input().strip().split())
skills = list(map(int, input().strip().split()))
skills.sort(reverse=True)
damage = 0
count_1 = m//(k+1)
count_2 = m%(k+1)
damage = count_1*(skills[0]*k+skills[1]) + count_2*skills[0]

print(damage)