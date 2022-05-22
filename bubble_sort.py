def bubble_sort(a:list):
    # сортировка списка a методом пузырька
    n = len(a)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]



def test_sort(sort_algorithm):
    print('=========================')
    print('Bubble sort test: ', end='')
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    # if a == a_sorted:
    #     print('OK')
    # else:
    #     print('FAIL')
    print('OK' if a == a_sorted else 'FAIL')

test_sort(bubble_sort)

# a = [1, 2, 3, 4, 2, 3, 4, 5, 6, 10, 22, 11, 23, 4, 342, 42, 1, 12, 0, 123, 55, 21, 123, 31]

# bubble_sort(a)
# print(a)