def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)
    def f(weights, x):
        days = 1
        current = 0
        for weight in weights:
            current += weight
            if current > x:
                days += 1
                current = weight
        return days

    while left <= right:
        mid = left + (right-left)//2
        e_days = f(weights,mid)
        print(mid, e_days)
        if e_days==days:
            right = mid - 1
        elif e_days>days:
            left = mid + 1
        elif e_days<days:
            right = mid - 1
    return left


weights = [1,2,3,1,1]
days = 4
res = shipWithinDays(weights,days)
print(res)