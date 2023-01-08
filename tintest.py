from timeit import timeit
def test_lev_dist(f: callable, a, b, n=1):
    tm = timeit("f(a, b)", globals={
        'f': f, 'a': a, 'b': b
    }, number=n)
    r = f(a, b)
    print(f'a = {a!r} and b = {b!r} and {f.__name__} = {round((r/max(len(a),len(b)))*100,3)}% and time = {tm:.4f}')
def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        # убедимся что n <= m, чтобы использовать минимум памяти O(min(n, m))
        a, b = b, a
        n, m = m, n
    current_row = range(n + 1)  # 0 ряд - просто восходящая последовательность (одни вставки)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]
t,r=input()
test_lev_dist(distance, t, r, n=10000)
