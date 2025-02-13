def cube(num):
    return num**3
def by_three(num):
    if num %3==0:
        return cube(num)
    else:
        return None

print(by_three(99))