def insertion_sort(a:list):
    # сортировка списка a вставками
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1

def test_sort(sort_algorithm):
    print('=========================')
    print('Insertion sort test: ', end='')
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    sort_algorithm(a)
    # if a == a_sorted:
    #     print('OK')
    # else:
    #     print('FAIL')
    print('OK' if a == a_sorted else 'FAIL')

test_sort(insertion_sort)
