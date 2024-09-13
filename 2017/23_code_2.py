def part2_dumb() -> int:
    a = 1
    b = 106_700
    c = 123_700
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

    while True:
        f = 1
        d = 2
        while True:
            e = 2

            while True:
                g = (d * e) - b
                if g == 0:
                    f = 0
                e += 1
                g = e - b
                if g == 0:
                    break
            d += 1
            g = d
            g -= b
            if g == 0:
                break

        if f == 0:
            h += 1
        g = b
        g -= c

        if g == 0:
            return h
        b += 17


# simplified...
def part2() -> int:
    b = 106_700
    c = 123_700
    d = 0
    f = 0
    g = 0
    h = 0

    while True:
        f = 1
        d = 2
        while True:
            if b % d == 0 and 2 <= b // d <= b:
                f = 0
                break

            d += 1
            if d == b:
                break

        if f == 0:
            h += 1
        g = b - c

        if g == 0:
            return h
        b += 17


print(f"Part 2: {part2()}")
