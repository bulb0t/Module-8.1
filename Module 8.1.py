a, b = 2, 'awdd'

def add_everything_up(m, n):
    try:
        return m + n
    except TypeError as exc:
        # print(f'Ошибка {exc}')
        return str(m) + str(n)

print(add_everything_up(a, b))