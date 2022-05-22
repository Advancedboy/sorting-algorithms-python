def selection_sort(a:list):
    # сортировка списка a выбором
    n = len(a)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def test_sort(sort_algorithm):
    print('=========================')
    print('Selection sort test: ', end='')
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(a)
    # if a == a_sorted:
    #     print('OK')
    # else:
    #     print('FAIL')
    print('OK' if a == a_sorted else 'FAIL')

test_sort(selection_sort)