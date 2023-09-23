def base(n) :
    total = 0
    x = "2"
    for i in range(n) :
        d = x*(i+1)
        total += int(d)
    return total

print(base(5))