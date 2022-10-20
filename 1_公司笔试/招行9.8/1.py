n = int(input())
print('z'*11)
recover = []
no_recover = []
for i in range(n):
    data.append(input().split())
    line = input().split()

    for item in line[1:]:
        if item=='?':
            count+=1

    name, s1, s2, s3, total_s = line
    if count == 0:
        recover.append([name, s1, s2, s3, total_s])
    elif count==1:
        if name == '?':
            name = 'z'*10
        elif total_s == '?':
            total_s = int(s1) + int(s2) + int(s3)
            recover.append([name, s1, s2, s3, total_s])
        else:
            if s1 == '?': s1 = int(total_s) - int(s2) - int(s3)
            if s2 == '?': s2 = int(total_s) - int(s1) - int(s3)
            if s3 == '?': s3 = int(total_s) - int(s1) - int(s2)
            recover.append([name, s1, s2, s3, total_s])
    else:
        no_recover.append([name, s1, s2, s3, total_s])

    sorted_cover = sorted(recover, lambda x:x[4], reverse=True)
    sorted_no = sorted(no_recover, lambda x:x[1])
