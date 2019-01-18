import cmath

def is_egg_broken(floor, breaking_point):
    if floor > breaking_point:
        return True
    else: return False

def calculate_interval(floors):
    # solving quadratic formula to find optimal initial interval
    # interval(interval+1) = 2* floors
    a = 1
    b = 1
    c = -2 * floors
    d = (b**2) - (4 * a * c)
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    sol1 = sol1.real
    sol2 = sol2.real
    if sol1 >= 0:
        return round(sol1)
    elif sol2 >= 0:
        return round(sol2)
    else:
        print('No real solution!')
        return None



def find_breaking_point(floors, breaking_point):
    interval = calculate_interval(floors)
    previous_floor = 0
    egg1 = interval

    #Drop egg1
    while is_egg_broken(egg1, breaking_point) is False and egg1 <= floors and interval >= 0:
        interval = interval - 1
        egg1 = egg1 + interval
        previous_floor = egg1

    #Drop egg2
    egg2 = previous_floor + 1

    while is_egg_broken(egg2, breaking_point) and egg2 <= egg1 and egg2 <= floors:
        egg2 =+ 1

    if egg2 > floors:
        print('Egg did not break at all!')
        return False

    else:
        return egg2

breaking_point = 75
floors = 100
egg2 = find_breaking_point(floors, breaking_point)

print('For a {} m building we have approximated actual breaking point {} m at {} m'.format(
    floors, breaking_point, egg2))