k, f = (int(i) for i in input().split())
while k not in range(1, (10 ** 18) + 1):
    print('введите k от 1 до 10**18')
    k = int(input())
while f not in range(2, (10 ** 5) + 1):
    print('введите f от 2 до 10**5')
    f = int(input())
if k == 1:
    print(0)
else:
    s = [1, 1]  # n = 1, f(n) =0 Долго мучился с Test 7.

    for i in range(2, f ** 2 + 1):
        s += [(s[i - 2] + s[i - 1]) % f]
        if s[i - 2] == 0 and s[i - 1] == 1:
            break

    h = [0] + s

    l = len(h) - 3

    q = k % l

    print(h[q])
